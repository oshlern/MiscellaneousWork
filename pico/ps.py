import socket, re

hostname = socket.gethostbyname('2018shell2.picoctf.com')
port = 7866

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hostname, port))
string = "Let\'s start with a warmup."
while True:
    print('hi')
    data = s.recv(1024)
    print(data)
    info = data[re.search(string, data).start()+len(string):]
    if  in data:
        break

