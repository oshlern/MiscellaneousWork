from tqdm import tqdm as ProgressDisplay
from scipy.stats import entropy
import os

MISS = 0
MISPLACED = 1
EXACT = 2

DATA_DIR = "wordle_data"
WORD_DATA_DIR = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    "wordle_data",
)
SHORT_WORD_LIST_FILE = os.path.join(WORD_DATA_DIR, "possible_words.txt")
LONG_WORD_LIST_FILE = os.path.join(WORD_DATA_DIR, "allowed_words.txt")
WORD_FREQ_FILE = os.path.join(WORD_DATA_DIR, "wordle_words_freqs_full.txt")
WORD_FREQ_MAP_FILE = os.path.join(WORD_DATA_DIR, "freq_map.json")
SECOND_GUESS_MAP_FILE = os.path.join(WORD_DATA_DIR, "second_guess_map.json")
PATTERN_MATRIX_FILE = os.path.join(DATA_DIR, "pattern_matrix.npy")
ENT_SCORE_PAIRS_FILE = os.path.join(DATA_DIR, "ent_score_pairs.json")

# To store the large grid of patterns at run time
PATTERN_GRID_DATA = dict()


def safe_log2(x):
    return math.log2(x) if x > 0 else 0


# Reading from files

def get_word_list(short=False):
    result = []
    file = SHORT_WORD_LIST_FILE if short else LONG_WORD_LIST_FILE
    with open(file) as fp:
        result.extend([word.strip() for word in fp.readlines()])
    return result


def get_word_frequencies(regenerate=False):
    if os.path.exists(WORD_FREQ_MAP_FILE) or regenerate:
        with open(WORD_FREQ_MAP_FILE) as fp:
            result = json.load(fp)
        return result
    # Otherwise, regenerate
    freq_map = dict()
    with open(WORD_FREQ_FILE) as fp:
        for line in fp.readlines():
            pieces = line.split(' ')
            word = pieces[0]
            freqs = [
                float(piece.strip())
                for piece in pieces[1:]
            ]
            freq_map[word] = np.mean(freqs[-5:])
    with open(WORD_FREQ_MAP_FILE, 'w') as fp:
        json.dump(freq_map, fp)
    return freq_map


def get_frequency_based_priors(n_common=3000, width_under_sigmoid=10):
    """
    We know that that list of wordle answers was curated by some human
    based on whether they're sufficiently common. This function aims
    to associate each word with the likelihood that it would actually
    be selected for the final answer.

    Sort the words by frequency, then apply a sigmoid along it.
    """
    freq_map = get_word_frequencies()
    words = np.array(list(freq_map.keys()))
    freqs = np.array([freq_map[w] for w in words])
    arg_sort = freqs.argsort()
    sorted_words = words[arg_sort]

    # We want to imagine taking this sorted list, and putting it on a number
    # line so that it's length is 10, situating it so that the n_common most common
    # words are positive, then applying a sigmoid
    x_width = width_under_sigmoid
    c = x_width * (-0.5 + n_common / len(words))
    xs = np.linspace(c - x_width / 2, c + x_width / 2, len(words))
    priors = dict()
    for word, x in zip(sorted_words, xs):
        priors[word] = sigmoid(x)
    return priors


def get_true_wordle_prior():
    words = get_word_list()
    short_words = get_word_list(short=True)
    return dict(
        (w, int(w in short_words))
        for w in words
    )


# String matching, etc.


def pattern_trit_generator(guess, true_word):
    for c1, c2 in zip(guess, true_word):
        if c1 == c2:
            yield EXACT
        elif c1 in true_word:
            yield MISPLACED
        else:
            yield MISS


def get_pattern(guess, true_word):
    """
    A unique integer id associated with the grey/yellow/green wordle
    pattern relatign a guess to the tue answer. In the ternary representation
    of this number, 0 -> grey, 1 -> yellow, 2 -> green.
    """
    return sum(
        value * (3**i)
        for i, value in enumerate(pattern_trit_generator(guess, true_word))
    )


def pattern_from_string(pattern_string):
    return sum((3**i) * int(c) for i, c in enumerate(pattern_string))


def pattern_to_int_list(pattern):
    result = []
    curr = pattern
    for x in range(5):
        result.append(curr % 3)
        curr = curr // 3
    return result


def pattern_to_string(pattern):
    d = {MISS: "⬛", MISPLACED: "🟨", EXACT: "🟩"}
    return "".join(d[x] for x in pattern_to_int_list(pattern))


def patterns_to_string(patterns):
    return "\n".join(map(pattern_to_string, patterns))


def patterns_hash(patterns):
    """
    Unique id for a list of patterns
    """
    return hash("".join(map(str, patterns)))
    # return sum((3**(5 * i) + 1) * (p + 1) for i, p in enumerate(patterns))


def generate_pattern_grid(words1, words2):
    """
    A pattern for two words represents the worle-similarity
    pattern (grey -> 0, yellow -> 1, green -> 2) but as an integer
    between 0 and 3^5. Reading this integer in ternary gives the
    associated pattern.

    This function computes the pairwise patterns between two lists
    of words, returning the result as a grid of hash values. Since
    this is the most time consuming part of many computations, all
    operations that can be are vectorized, perhaps at the expense
    of easier readibility.
    """
    # Convert word lists to integer arrays
    w1, w2 = (
        np.array([[ord(c) for c in w] for w in words], dtype=np.uint8)
        for words in (words1, words2)
    )

    if len(w1) == 0 or len(w2) == 0:
        return np.zeros((len(w1), len(w2)), dtype=np.uint8)

    # equality_grid[a, b, i, j] represents whether the ith letter
    # of words1[a] equals the jth letter of words2[b]
    equality_grid = np.zeros((len(w1), len(w2), 5, 5), dtype=bool)
    for i, j in it.product(range(5), range(5)):
        equality_grid[:, :, i, j] = np.equal.outer(w1[:, i], w2[:, j])

    patterns = np.zeros((len(w1), len(w2)), dtype=np.uint8)
    three_pows = (3**np.arange(5)).astype(np.uint8)
    for i, tp in enumerate(three_pows):
        # This accounts for yellow squares
        patterns[:, :] += tp * equality_grid[:, :, i, :].any(2)
        # This accounts for green squares
        patterns[:, :] += tp * equality_grid[:, :, i, i]

    return patterns


def generate_full_pattern_grid():
    words = get_word_list()
    grid = generate_pattern_grid(words, words)
    np.save(PATTERN_MATRIX_FILE, grid)


def get_pattern_grid(words1, words2):
    if not PATTERN_GRID_DATA:
        if not os.path.exists(PATTERN_MATRIX_FILE):
            log.info("Generating pattern matrix...(this takes a moment, but is only needed once)")
            generate_full_pattern_grid()
        PATTERN_GRID_DATA['grid'] = np.load(PATTERN_MATRIX_FILE)
        PATTERN_GRID_DATA['words_to_index'] = dict(zip(
            get_word_list(), it.count()
        ))

    full_grid = PATTERN_GRID_DATA['grid']
    words_to_index = PATTERN_GRID_DATA['words_to_index']

    indices1 = [words_to_index[w] for w in words1]
    indices2 = [words_to_index[w] for w in words2]
    return full_grid[np.ix_(indices1, indices2)]


def get_possible_words(guess, pattern, word_list):
    all_hashes = get_pattern_grid([guess], word_list).flatten()
    return list(np.array(word_list)[all_hashes == pattern])


def get_word_buckets(guess, possible_words):
    buckets = [[] for x in range(3**5)]
    hashes = get_pattern_grid([guess], possible_words).flatten()
    for index, word in zip(hashes, possible_words):
        buckets[index].append(word)
    return buckets

