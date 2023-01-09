import os , socket , time
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind((socket.gethostname(),8000))
sock.listen(5)
print("HOST : ",sock.getsockname())

client, addr = sock.accept()

file_name = input("File Name : ")
file_size = os.path.getsize(file_name)

#hosting file 

client.send(file_name.encode())
client.send(str(file_size).encode())

with open (file_name,"rb") as file :
    begin_size = 0

    start = time.time()

    while begin_size <= file_size :
        data = file.read(1024)
        if not (data) : 
            break
        client.sendall(data)
        begin_size+= len(data)
       
    end = time.time()

print("file transfer is complete : ", end-start)