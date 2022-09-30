from queue import Empty
from time import sleep
from colorama import Fore , Style ,init,deinit


deinit()
init()

mylistnumber = ['test']




 
numberss ={"Amal":564215458,
"Mohammed":555652458,
"Khadijah":558741574,
"Abdullah":548745965,
"Rawan":	5555555555,
"Faisal":	536214525,
"Layla":	596545625}

def cheaknumbers(addnumberss):
    for i in numberss.values():
        if i == addnumberss:
            
            return i

def color():
    menu = f'''{Fore.LIGHTRED_EX}
                                                ╔══════════════════════════════╗
                                                  [1]      Add Number
                                                  [2]      delet number
                                                  [3]      cheak number
                                                  [4]      Exit
                                                ╚══════════════════════════════╝    {Style.RESET_ALL} '''
    return menu

def welcome():
    
    print(color())
    
    select = input(" Select from list what you want : ")
    if select == "1" or select == 1:
        newnumber = int(input("  add number only 10 numbers : "))
        newname = input(" add name for that number only one name : ")
        
        if cheaknumbers(newnumber) == newnumber:
          print(f"{Fore.LIGHTRED_EX} ## number ready add before ##{Style.RESET_ALL}")
          welcome()
        elif len(str(newnumber)) == 9:
            up_dict = {f"{newname}":newnumber}
            numberss.update(up_dict)
            print(f"{Fore.LIGHTGREEN_EX} ## done number is added ## {Style.RESET_ALL}")
            welcome()
        else:
            welcome()
            print("have error call the king")
    elif select == 2 or select == "2":
        newnumberdel = int(input("  add number only 10 numbers : "))
        if cheaknumbers(newnumberdel) == newnumberdel:
         
         del numberss[list(numberss.keys())[list(numberss.values()).index(newnumberdel)]]
         print(f"{Fore.LIGHTGREEN_EX} ## Number is deleted ## {Style.RESET_ALL}")
         welcome()
        else :
            print(f"{Fore.LIGHTRED_EX} ## ERROR ##{Style.RESET_ALL}")
            welcome()
    elif select =="3" or select == 3:
        for gg,tt in numberss.items():
            print(f"{Fore.LIGHTYELLOW_EX} # Names :  {gg} {Style.RESET_ALL}  {Fore.LIGHTGREEN_EX}    {0}{tt}  {Style.RESET_ALL}")
        welcome()
    elif select == 4 or select =="4":
        exit()
    else:
        print(f"{Fore.LIGHTRED_EX} ## ERROR Call TheKing ##{Style.RESET_ALL}")
        welcome()
             
welcome()
