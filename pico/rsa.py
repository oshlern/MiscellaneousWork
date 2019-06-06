from sympy import mod_inverse

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m
# print(d('llkjmlmpadkkc', 'thisisalilkey'))


def gcd(a, b):
    """Return greatest common divisor using Euclid's Algorithm."""
    while b:      
        a, b = b, a % b
    return a

def lcm(a, b):
    """Return lowest common multiple."""
    return a * b // gcd(a, b)

print(lcm(93187, 94603))
print((78203-1)*(79999-1))
y = pow(1815907181716474805136452061793917684000871911998851410864797078911161933431337632774829806207517001958179617856720738101327521552576351369691667910371502971480153619360010341709624631317220940851114914911751279825748,3,29129463609326322559521123136222078780585451208149138547799121083622333250646678767769126248182207478527881025116332742616201890576280859777513414460842754045651093593251726785499360828237897586278068419875517543013545369871704159718105354690802726645710699029936754265654381929650494383622583174075805797766685192325859982797796060391271817578087472948205626257717479858369754502615173773514087437504532994142632207906501079835037052797306690891600559321673928943158514646572885986881016569647357891598545880304236145548059520898133142087545369179876065657214225826997676844000054327141666320553082128424707948750331)
print("y", y)
print("")
x = (92092076805892533739724722602668675840671093008520241548191914215399824020372076186460768206814914423802230398410980218741906960527104568970225804374404612617736579286959865287226538692911376507934256844456333236362669879347073756238894784951597211105734179388300051579994253565459304743059533646753003894559-1)*(97846775312392801037224396977012615848433199640105786119757047098757998273009741128821931277074555731813289423891389911801250326299324018557072727051765547115514791337578758859803890173153277252326496062476389498019821358465433398338364421624871010292162533041884897182597065662521825095949253625730631876637-1)
a = modinv(65537,x)
print("modinv", a)

n = 23952937352643527451379227516428377705004894508566304313177880191662177061878993798938496818120987817049538365206671401938265663712351239785237507341311858383628932183083145614696585411921662992078376103990806989257289472590902167457302888198293135333083734504191910953238278860923153746261500759411620299864395158783509535039259714359526738924736952759753503357614939203434092075676169179112452620687731670534906069845965633455748606649062394293289967059348143206600765820021392608270528856238306849191113241355842396325210132358046616312901337987464473799040762271876389031455051640937681745409057246190498795697239
p = 153143042272527868798412612417204434156935146874282990942386694020462861918068684561281763577034706600608387699148071015194725533394126069826857182428660427818277378724977554365910231524827258160904493774748749088477328204812171935987088715261127321911849092207070653272176072509933245978935455542420691737433 
c = 14699632914289984358210582075909309608817619615764122409514577850253033131275996955127394794512801987443786025277031557775238937388086632327611216460613138074110905840487213116627139558528011448028813522809156509374602431319619052803531008581645459969997969897966475478980398396687104746302415391434104278327526947341073215599683555703818611403510483832532921625745935543818100178607417658929607435582550913918895885596025822532531372429301293588416086854338617700672628239475365045267537032531973594689061842791028000992635092519215619497247452814483357403667400283975070444902253349175045305073603687442947532925780
e = 65537
q = 156408916769576372285319235535320446340733908943564048157238512311891352879208957302116527435165097143521156600690562005797819820759620198602417583539668686152735534648541252847927334505648478214810780526425005943955838623325525300844493280040860604499838598837599791480284496210333200247148213274376422459183
# print("test", n%p)
# q = int(n/p)
print(n-q*p)
print("q", q, q%2)
d = mod_inverse(e, lcm(p-1,q-1))
print(d)
m = pow(c,d,n)
print("M, ")
print(m)