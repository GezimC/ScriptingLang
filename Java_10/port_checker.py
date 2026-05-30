import socket as s


HOST = '127.0.0.1'
PORTS = ['80','22','443', '5432']
TIME_OUT_SECONDS = 1

sock = s.socket()
result = sock.connect_ex(('178.132.223.152', 3001))
sock.settimeout(1)
sock.close()

if result == 0:
    print("Port open")
else:
    print("Port closed")



 # def check_port(host, port)

 # def scan_ports(host, ports)




