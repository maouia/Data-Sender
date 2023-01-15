import os,socket,time


def Resive():
    host = input("Enter Host Sender : ")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        sock.connect((host, 8001))
        print("connected")
    except:
        print("Unable to connect")
        exit()

    # recive file from host
    file_name = sock.recv(4096).decode()
    file_size = sock.recv(100).decode()
    
    file_size=int(file_size)
    file_name.replace(str(file_size), '')

    # Create folder and white the file inside
    with open('./' + file_name, 'wb') as file:
        begin_size = 0

        start = time.time()

        while begin_size <= int(file_size):
            data = sock.recv(1024)
            if not (data):
                break
            file.write(data)
            begin_size += len(data)
        end = time.time()
    print("File transfer complete. Total time : ", end - start)


def Send() :

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((socket.gethostname(), 8001))
    sock.listen(5)
    print("HOST : ", sock.getsockname())

    client, addr = sock.accept()

    file_name = input("File Name : ")
    file_size = os.path.getsize(file_name)

    # hosting file
    client.send(file_name.encode())
    client.send(str(file_size).encode())

    with open(file_name, "rb") as file:
        begin_size = 0

        start = time.time()

        while begin_size <= file_size:
            data = file.read(1024)
            if not (data):
                break
            client.sendall(data)
            begin_size += len(data)

        end = time.time()

    print("file transfer is complete : ", end - start)



while True :
    os.system("cls")
    x = input(" 1: Send \n 2: Recive \n 3: Exit ")
    match x : 
        case "1" : 
            Send()
        case "2" :
            Resive()
        case "3" :
            exit()
        case _:
            print("Unvalid choice")





