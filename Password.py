from colorama import Fore, Back, Style 
import time 
import os 
import random 

# MINE
from Caesar import Caesar
from Menu import Menu
# -----------------------------------

class Password:
    """
    This class is for the creation of the user's account, 
    and for the user to log in to this "password manager" account.

    METHODS (3)
    - check_if_account_exists()
    - <MAIN, one time> account_setup()
        * used for the first time, when user didnt create an account yet
        * used one time per user

    - <MAIN> login()
    """

    def __init__(self):
        pass 
    # ===============================================

    def check_if_account_exists(self) -> bool:
        valid_setup = False 
        if (os.path.exists("files/setup") and os.path.exists("files/key")):
            valid_setup = True 
            with open("files/setup", mode="r") as r:
                data = r.readlines()
            
            try: 
                print(data[2].strip("\n"))
                valid_setup = True 
            except: 
                pass 

        return valid_setup
    # ===============================================

    def account_setup(self) -> None:
        print("\nCREATE ACCOUNT\n")

        account_exists = False 
        while not account_exists:
            username = input("Create your username: ")
            password = input("Create your password: ")
            retype_password = input("Confirm your password: ")

            if password != retype_password:
                print(f"{Fore.RED}Passwords do not match{Fore.RESET}\n")

            else:
                print(f"{Fore.YELLOW + Style.BRIGHT}\nYour account has successfully been created{Fore.RESET}")
                print(f"\n{Back.CYAN}Remember the created username and password, as this is what you need to view your other account info{Back.RESET + Style.RESET_ALL}")
                print(f"Username: {username}")
                print(f"Password: {password}")

                time.sleep(1)
                # input("Close and rerun the application to continue...\n")
                account_exists = True 
                print()
        
        # selected_option = self.encryption_complexity()

        # create setup file
        with open("files/setup", mode="w") as w:
            w.write(f"{username}\n")
            w.write(f"{password}\n")
            # w.write(f"{selected_option},\n")

        with open("files/key", mode="w") as key:
            key.write(f"{username[0]}\n")
            key.close()


        obj = Caesar()
        # encrypting setup file
        obj.encrypt_write("files/setup", "files/setup", username[0])

        # adding and encrypting to the accounts doc
        with open("temp_acc.txt", mode="w") as acc:
            acc.write("temp: [temp, data]")
        obj.encrypt_write("temp_acc.txt", "files/acc.txt", username[0])

        # removing temp file
        os.remove("temp_acc.txt")

        print("\n<process complete>")
        time.sleep(1)
        print("\n<rerun to login>")
        time.sleep(1)
    # ===============================================

    def login(self) -> None:
        alpha = "abcdefghijklmnopqrstuvwxyz"

        # title
        print("\nLOGIN")

        # decrypting
        with open("files/key", mode="r") as r:
            key = r.readlines()
        
        # determining complexity level
        # key_complexity = (key[1].strip("\n"))
        # print(key_complexity)

        key_num = alpha.index(key[0].lower().strip("\n"))
        obj = Caesar()
        obj.decrypt("files/setup", "files/temp_setup", key_num)

        with open("files/temp_setup", mode="r") as r:
            lines = r.readlines()

        password = lines[1].strip("\n")
        print(password)

        # removing temp file
        os.remove("files/temp_setup")

        # loop
        chances = 3 
        while chances > 0:
            # random code
            code = str(random.randint(100, 1000)) + "_"
            for i in range(9):
                a = random.choice(list(alpha))
                code += a 

            # enter_usrnm = input("\nEnter your username: ")
            MASTER_PSWD = input("\nEnter your password: ")
            # correct password
            if MASTER_PSWD == password:
                print("\n",code)
                print("\nEnter the given code")
                is_code = input("> ")
                if is_code == code:
                    # chances = 0
                    chances -= chances
                    os.system("cls")
                    time.sleep(1)

                    # creating Menu obj
                    obj1 = Menu()
                    obj1.menu()

                else:
                    chances -= 0.5
                    print(f"{Fore.RED + Style.BRIGHT}incorrect code{Fore.RESET + Style.RESET_ALL}")
                    print(f"{Fore.RED + Style.BRIGHT}{chances} more attempts{Fore.RESET + Style.RESET_ALL}")


            # final chance
            elif MASTER_PSWD != password and chances == 2:
                print(f"{Fore.RED + Style.BRIGHT}one more chance{Fore.RESET + Style.RESET_ALL}")
                chances -= 1


            else:
                print(f"{Fore.RED + Style.BRIGHT}incorrect password{Fore.RESET + Style.RESET_ALL}")
                chances -= 1
    # ===============================================
# ***************************************************

# obj = Password()
# print(help(obj))
# ***************************************************