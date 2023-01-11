import os , socket , time

host = input("Enter Host Sender : ")
socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try : 
    socket.connect((host,8000))
    print("connected")
except : 
    print("Unable to connect")
    exit()


#recive file from host
file_name= socket.recv(100).decode()
file_size = socket.recv(100).decode()

#Create folder and white the file inside
with open('./'+file_name,'wb') as file :
    begin_size = 0

    start = time.time()

    while begin_size <= int(file_size) :
        os.system("cls")
        print(begin_size ," / ", int(file_size))
        data=socket.recv(1024)
        
        if not (data):
            break
        file.write(data)
        begin_size += len(data)


    end = time.time()

print("File transfer complete. Total time : ",end-start)