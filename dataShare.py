import os


while True :
    os.system("cls")
    x = input(" 1: Send \n 2: Recive \n 3: Exit ")
    match x : 
        case "1" : 
            import Sender 
        case "2" :
            import Reciever 
        case "3" :
            exit()
        case _:
            print("Unvalid choice") 