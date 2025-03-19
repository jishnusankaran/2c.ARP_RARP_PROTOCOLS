 
import socket 
s=socket.socket() 
s.connect(('localhost',8000)) 
while True: 
 

    ip=input("Enter MAC Address : ") 
    s.send(ip.encode()) 
    print("Logical Address",s.recv(1024).decode())