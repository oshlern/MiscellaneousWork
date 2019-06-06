import string

k = int(input())
m = input()

out = ""
for mi in m:
	if mi in string.ascii_lowercase:
		out += string.ascii_lowercase[(string.ascii_lowercase.index(mi) - k)%len(string.ascii_lowercase)]
	elif mi in string.ascii_uppercase:
		out += string.ascii_uppercase[(string.ascii_uppercase.index(mi) - k)%len(string.ascii_uppercase)]
	else:
		out += mi
print(out)