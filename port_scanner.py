import socket

asking = input("Which IP you want to scan? ")
for i in range (1,1025):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.1)
    z = s.connect_ex((asking,i))
    if z == 0:
      print("Port", i, "is Open")
    s.close()
    