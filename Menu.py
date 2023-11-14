from colorama import Fore, Back, Style 
import random
import time 
import os 
# from cryptography.fernet import Fernet

# MINE
from Caesar import Caesar
# ============================================================


class Menu:
    """
    The class is

    temp -> file for temp data 
    """

    def __init__(self):
        self.options = {
            "1": self.view_acc,
            "2": self.edit_acc,
            "3": self.add_acc,
            "4": self.remove_acc 
        }
        self.close_words = ["esc", "escape", "quit", "leave", "exit", "close"]
        self.accounts = {}
        
    # ===============================================

    # reading the plain-text file
    def reading_accounts(self, file_enc="file.txt") -> None:
        obj = Caesar()

        # creating temp file; deleted at the end
        with open("temp", mode="w") as temp:
            temp.write("temp: [temp, data]")

        # getting key
        alpha = "abcdefghijklmnopqrstuvwxyz"
        with open("files/key", mode="r") as read_key:
            key = read_key.readlines()
        key_num = alpha.index(key[0].lower().strip("\n"))

        # decrypting
        obj.decrypt(file_enc, "temp", key_num)

        # adding accounts to dict
        with open("temp", "r") as file:
            f = file.readlines()

            for i in f:
                if i != "\n":
                    i = i.strip("\n")
                    stop = i.index(":")
                    # print(stop)

                    acc_key = i[0:stop]
                    acc_value = i[(stop+2)::]

                    self.accounts[acc_key] = acc_value

        # print(self.accounts)
    # ===============================================


    def view_acc(self) -> None:
        print(f"{Fore.CYAN + Style.BRIGHT}\nVIEW ACCOUNT DETAILS{Fore.RESET}")

        # view all possible platform
        print(f"\n{Back.WHITE}Type 'list' to view all websites or platforms{Back.RESET + Style.RESET_ALL}")

        exit = False 
        while not exit:
            select = input("\nEnter a website/ platform name: ")
            try:
                if select in ["esc", "escape", "quit", "exit", "leave"]:
                    exit = True 
                    os.system("cls")
                    # menu()

                # listing all platform names
                elif select == "list":
                    print(Fore.GREEN)
                    a = self.accounts.keys()

                    platforms = []

                    for aa in a:
                        platforms.append(aa)

                    # printing platforms
                    platforms.sort()
                    for p in platforms:
                        print(p)
                        time.sleep(0.001)

                    print(Fore.RESET)

                    print(f"{len(platforms)} accounts\n")


                else:
                    print(self.accounts[select])


            except KeyError:
                print(f"{Fore.RED}invalid input{Fore.RESET}")
    # ===============================================

    def edit_acc(self) -> None:
        print(f"{Fore.CYAN + Style.BRIGHT}\nEDIT ACCOUNT DETAILS{Fore.RESET}")

        # view all possible platform
        print(f"\n{Back.WHITE}Type 'list' to view all websites or platforms{Back.RESET + Style.RESET_ALL}")
        
        exit = False 
        while not exit:
            select = input("\nEnter the platform name to edit the details: ")

            try:
                if select in ["esc", "escape", "quit", "exit", "leave"]:
                    os.system("cls")
                    exit = True 

                # listing all platform names
                elif select == "list":
                    print(Fore.GREEN)
                    a = self.accounts.keys()

                    platforms = []

                    for aa in a:
                        platforms.append(aa)

                    # printing platforms
                    platforms.sort()
                    for p in platforms:
                        print(p)
                        time.sleep(0.01)

                    print(Fore.RESET)

                # edit details
                elif select in self.accounts.keys():
                    print(self.accounts[select])

                    username = input("Enter the new username: ")
                    password = input("Enter the new password: ")
                    self.accounts[select] = [username, password]

                    # adding new data to txt file
                    f = open("temp", "a")
                    f.write(f"{select}: {[username, password]}\n")

                    print(f"\n{Fore.YELLOW}Details modified!{Fore.RESET}")
                    print(self.accounts[select])

                
                else:
                    print(self.accounts[select])
                    # print(f"{Fore.RED}invalid input{Fore.RESET}")
                    

            except KeyError:
                print(f"{Fore.RED}invalid input{Fore.RESET}")
    # ===============================================

    def add_acc(self) -> None:
        print(f"{Fore.CYAN + Style.BRIGHT}\nADD ACCOUNT DETAILS{Fore.RESET}")

        # view all possible platform
        print(f"\n{Back.WHITE}Type 'list' to view all websites or platforms{Back.RESET + Style.RESET_ALL}")

        exit = False 
        while not exit:
            select = input("\nEnter a NEW website/ platform name: ")

            try:
                if select in ["esc", "escape", "quit", "exit", "leave"]:
                    exit = True 
                    os.system("cls")


                # listing all platform names
                elif select == "list":
                    print(Fore.GREEN)
                    a = self.accounts.keys()

                    platforms = []
                    for aa in a:  platforms.append(aa)

                    # printing platforms
                    platforms.sort()
                    for p in platforms:
                        print(p)
                        time.sleep(0.01)

                    print(Fore.RESET)


                # already exists
                elif select in self.accounts.keys():
                    print("\nPlatform already exists in database")
                    
                
                # adding details
                else:
                    username = input("Enter the new username: ")
                    password = input("Enter the new password: ")
                    self.accounts[select] = [username, password]

                    # adding new data to txt file
                    f = open("temp", "a")
                    f.write(f"{select}: {[username, password]}\n")

                    print(f"\n{Fore.YELLOW}Details added!{Fore.RESET}")
                    print(self.accounts[select])


            except KeyError:
                print(f"{Fore.RED}invalid input{Fore.RESET}")
    # ===============================================

    def remove_acc(self) -> None:
        print(f"{Fore.CYAN + Style.BRIGHT}\nREMOVE ACCOUNT DETAILS{Fore.RESET}")

        # view all possible platform
        print(f"\n{Back.WHITE}Type 'list' to view all websites or platforms{Back.RESET + Style.RESET_ALL}")

        exit = False 
        while not exit:
            select = input("\nEnter a website/ platform name to remove: ")

            try:
                if select in ["esc", "escape", "quit", "exit", "leave"]:
                    exit = True 
                    os.system("cls")
                    # menu()


                # listing all platform names
                elif select == "list":
                    print(Fore.GREEN)
                    a = self.accounts.keys()

                    platforms = []
                    for aa in a: platforms.append(aa)

                    # printing platforms
                    platforms.sort()
                    for p in platforms:
                        print(p)
                        time.sleep(0.1)

                    print(Fore.RESET)

                
                else:
                    print(self.accounts[select])
                    print("Are you sure you want to remove this account? (y/n)")

                    confirmation = input("> ").lower()
                    if confirmation == "y":
                        alpha = "abcdefghijklmnopqrstuvwxyz"
                        # maybe add, enter the following code, or enter the password, or something
                        pswd1 = str(random.randint(100, 1000)) + "_"
                        for i in range(9):
                            a = random.choice(list(alpha))
                            pswd1 += a 
                        print(pswd1)

                        layer1 = input("\nenter the given code: ")
                        if layer1 == pswd1:
                            # clearing all data from text file
                            clear = open("data.txt", "w")
                            clear.write("")


                            # dictionary.pop(key_to_remove, not_found)
                            self.accounts.pop(select, "key not found")
                            
                            # adding new data to txt file
                            a = self.accounts.keys()

                            platforms = []
                            for aa in a: platforms.append(aa)

                            # printing platforms
                            platforms.sort()
                            for p in platforms:
                                print(p)
                                time.sleep(0.1)

                                with open("data.txt", "a") as f:
                                    f.write(f"{p}: {self.accounts[p]}\n")

                            print(f"\n{Back.YELLOW}Account removed{Back.RESET}")


                            print("\nNavigate to main menu? (y/n)")
                            leave_session = input("> ").lower()
                            if leave_session == "y":
                                exit = True 
                                os.system("cls")
                                # menu()


            except KeyError:
                print(f"{Fore.RED}invalid input{Fore.RESET}")
    # ===============================================

    def filter_account_names(self):
        # reading temp file
        account_names = set()
        with open("temp", mode="r") as r:
            rr = r.readlines()
        
        for re in rr:
            # print(re.split(":"))
            account_name = re.split(":")[0]
            account_names.add(account_name)
      

        # rewriting to temp file
        with open("temp", mode="w") as t:
            for line in rr:
                acc_name = line.split(":")[0]
                print(acc_name)

                if acc_name in account_names:
                    t.write(line)
                    account_names.remove(acc_name)
                    print("--sss")

    # ===============================================

 
    def overwrite_level1(self) -> None:
        # get key
        in_key = "j"
        with open("files/key", mode="r") as k:
            key = k.readlines()

        # encrypt data
        obj = Caesar()
        data = obj.encrypt_write(input_file="temp", dest_file="files/acc.txt", key=in_key)

        # overwriting to text file
        # file = open(f"files/acc", "w")
        # file.write(f"\n{data}\n")
    # ===============================================


    # MAIN MENU
    def menu(self) -> None:
       

        # adding accounts to file
        self.reading_accounts("files/acc.txt")

        # --testing
        self.filter_account_names()

        # title
        print(f"\n{Fore.GREEN + Style.BRIGHT}ACC0UNT MANAGER{Fore.RESET}")

        # MAIN LOOP
        user_left = False
        while not user_left:
            print(f"\n{Fore.GREEN + Style.BRIGHT}Main Menu{Fore.RESET}")

            print("\n1. View account")    
            print("2. Edit account")    
            print("3. Add account")    
            print("4. Remove account")    

            print(f"\n{Back.WHITE}Type 'ESC' to close the app, or to return to a previous section{Back.RESET + Style.RESET_ALL}")
            print(Style.RESET_ALL)

            # user input
            main_selection = input("\n> ")
            
            # exit 
            if main_selection in self.close_words:
                confirmation = input("Are you sure? (y/n) ").lower()
                if confirmation == "y":
                    # leaving loop
                    user_left = True 

                    # encrypting
                    self.overwrite_level1()

                    # deleting temp file
                    os.remove("temp")

            # options
            elif main_selection in self.options.keys():
                self.options[main_selection]()

            else:
                print(f"{Fore.RED}invalid input{Fore.RESET}")

    # ===============================================

# ***************************************************

# obj = Menu()

# obj.reading_accounts()
# obj.menu()
# ***************************************************