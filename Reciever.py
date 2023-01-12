import os,socket,time

host = input("Enter Host Sender : ")
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try : 
    sock.connect((host,8021))
    print("connected")
except : 
    print("Unable to connect")
    exit()


#recive file from host
file_name= sock.recv(4096).decode()
file_size = sock.recv(4096).decode()

file_name.replace(file_size,'')


#Create folder and white the file inside
with open('./'+file_name,'wb') as file :
    begin_size = 0

    start = time.time()


    while begin_size <= int(file_size) :
        data=sock.recv(1024)
        if not (data):
            break
        file.write(data)
        begin_size += len(data)
    end = time.time()

print("File transfer complete. Total time : ",end-start)