import socket

hostname = socket.gethostbyname('c1.easyctf.com')
port = 12487

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hostname, port))
# while True:
	# data = s.recv(1024)
	# if "encrypt(key, P255)" in data.decode():
	# 	break

# a = '1' + '0'*255
outs = []
for i in range(255):
	while True:
		data = s.recv(1024)
		# print data
		if 'Input plaintext ' + str(i) + ':' in data:
			break
	out = ''
	for j in range(256):
		if j == i:
			out += '1'
		else:
			out += '0'
	# print out
	outs.append(out)
	s.sendall(out + '\n')

while True:
	data = s.recv(1024)
	if 'Input plaintext ' + str(255) + ':' in data:
		break
out = ''
for j in range(256):
	if j == 255:
		out += '0'
	else:
		out += '1'
print out
outs.append(out)
s.sendall(out + '\n')

x = 0
for out in outs:
	x ^= int(out, 2)
print x
for i in range(3):
	print s.recv(1024)
