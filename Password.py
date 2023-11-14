from colorama import Fore, Back, Style 
from cryptography.fernet import Fernet
import time 
import os 
import random 

# MINE
from Caesar import Caesar
from Menu import Menu
# -----------------------------------

class Password:
    """
    This class 

    """

    def __init__(self):
        # self.key = ""
        self.options = {
            "1": "primative (level 1)",
            "2": "primative (level 2)",
            # "3": "highly secure"
        }
    # ===============================================


    def encryption_complexity(self) -> str:
        print("\nENCRPYTION COMPLEXITY\n")
        for option in self.options:
            print(F"{option}) {self.options[option]}")

        correct_option = False 
        while not correct_option:
            user_option = input("\nSelect an option: ")
            if user_option in self.options.keys():
                correct_option = True 

            else:
                print("*invalid option*")

        return user_option
    # ===============================================

    
    # def set_key(self, in_key):
    #     self.key = in_key
    # # ===============================================

    # def get_key(self):
    #     return self.key 
    # ===============================================

    
    def check_if_account_exists(self) -> bool:
        valid_setup = False 
        # print(os.path.exists("setup"))

        # reading file
        try:
            with open("files/setup", mode="r") as r:
                data = r.readlines()

            try: 
                print(data[2].strip("\n"))
                valid_setup = True 

            except: valid_setup = False

        except:
            print("file not found")
            valid_setup = False

        # return os.path.exists("setup")
        return valid_setup
    # ===============================================

    def check_if_account_exists1(self) -> bool:
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

        # # reading file
        # try:
        #     with open("files/setup", mode="r") as r:
        #         data = r.readlines()

        #     try: 
        #         print(data[2].strip("\n"))
        #         valid_setup = True 

        #     except: valid_setup = False

        # except:
        #     print("file not found")
        #     valid_setup = False

        # return os.path.exists("setup")
        # return valid_setup
    # ===============================================


    # for option3
    # check if key and master password exists
    # password section, using fernet, using hashed passwords
    # def option3_encrypt(self) -> None:
    #     # generating and saving the key
    #     key = Fernet.generate_key()
    #     with open("_key.key", "wb") as key_file:
    #         key_file.write(key)


    #     # encrypting username
    #     f = Fernet(key)
    #     b = bytes(username, 'utf-8')

    #     usrnm_encrypt = f.encrypt(b)
    #     # print(usrnm_encrypt)

    #     # encrypting password
    #     # key = Fernet.generate_key()
    #     f = Fernet(key)
    #     b = bytes(password, 'utf-8')

    #     pswd_encrypt = f.encrypt(b)
    #     # print(pswd_encrypt)


    #     # writing to a file
    #     with open("_usrnm.key", "wb") as locked_u:
    #         locked_u.write(usrnm_encrypt)
        
    #     with open("_pswd.key", "wb") as locked_p:
    #         locked_p.write(pswd_encrypt)


    #     # hiding file
    #     os.system("attrib +h _key.key")
    #     os.system("attrib +h _usrnm.key")
    #     os.system("attrib +h _pswd.key")
    # # ===============================================

    # # def password_check_if_exists(self) -> None:
    # def option3_decrypt(self) -> None:
    #     # from os.path import exists
    #     u = "_usrnm.key"
    #     p = "_pswd.key"
    #     k = "_key.key"

    #     u_exists = exists(u)
    #     p_exists = exists(p)
    #     k_exists = exists(k)

    #     if u_exists and p_exists and k_exists:

    #         # getting key and details
    #         f = open("_usrnm.key", "rb")
    #         cryp_usr = f.read()

    #         g = open("_pswd.key", "rb")
    #         cryp_pswd = g.read()
                
    #         with open("_key.key", "rb") as read_pswd:
    #             file = read_pswd.read()
    #             # print(type(file))
    #             f = Fernet(file)

    #             a = f.decrypt(cryp_usr)
    #             username = a.decode()

    #             b = f.decrypt(cryp_pswd)
    #             password = b.decode()

    #             # print(username)
    #             # print(password)

                
    #         # loop
    #         chances = 3 
    #         while chances > 0:

    #             # random code
    #             alpha = "abcdefghijklmnopqrstuvwxyz"
    #             code = str(random.randint(100, 1000)) + "_"
    #             for i in range(9):
    #                 a = random.choice(list(alpha))
    #                 code += a 

    #             # enter_usrnm = input("\nEnter your username: ")
    #             MASTER_PSWD = input("\nEnter your password: ")
    #             if MASTER_PSWD == password:
    #                 print(code)

    #                 print("\nEnter the given code")
    #                 is_code = input("> ")
    #                 if is_code == code:
    #                     # chances = 0
    #                     chances -= chances

    #                     os.system("cls")
    #                     time.sleep(1)
    #                     menu()

    #                 else:
    #                     print(f"{Fore.RED + Style.BRIGHT}incorrect code{Fore.RESET + Style.RESET_ALL}")
    #                     print(f"{Fore.RED + Style.BRIGHT}{chances} more attempts{Fore.RESET + Style.RESET_ALL}")
    #                     chances -= 0.5


    #             # final chance
    #             elif MASTER_PSWD != password and chances == 2:
    #                 print(f"{Fore.RED + Style.BRIGHT}final chance{Fore.RESET + Style.RESET_ALL}")
    #                 chances -= 1


    #             else:
    #                 print(f"{Fore.RED + Style.BRIGHT}incorrect password{Fore.RESET + Style.RESET_ALL}")
    #                 chances -= 1


    #     elif u_exists and not p_exists:
    #         print("u -", u_exists)
    #         print("p -", p_exists)
    #         print("a file might be missing")
        
    #     elif not u_exists and p_exists:
    #         print("u -", u_exists)
    #         print("p -", p_exists)
    #         print("a file might be missing")

    #     else:
    #         print()
    #         print(f"{Back.YELLOW + Style.BRIGHT} You don't have a password {Back.RESET + Style.RESET_ALL}\n")
    #         time.sleep(2)

    #         from create_account import create_acc
    #         create_acc() 
    # # ===============================================

    # for option2
    def option2_ascii_encode(self, file_in="data_encoded.txt", file_dest="data_encoded.txt"):
        with open(file_in, "r") as f:
            lines = f.readlines()
            content = []
            for l in lines:
                if l != "\n":
                    l = l.strip("\n")
                    content.append(l)
                    # print(len(l))


        # writing
        with open(file_dest, "w") as nums:
            ascii_list = []
            for string in content:
                for char in string:
                    a = ord(char)
                    ascii_list.append(a)
                    nums.write(str(a))
                    nums.write("\n")

        # print("<process complete>")
        # print(ascii_list)
    # ===============================================

    def option2_ascii_decode(self, file_in="ascii.txt", file_dest="d_encoded.txt"):
        with open(file_in, "r") as asc:
            plain = []
            lines = asc.readlines()

            # writing to a new file
            f = open(file_dest, "w")
            for num in lines:
                num = num.strip("\n")
                a = ord("]")
                if num == str(a):
                    char = chr(int(num))
                    print(char, end="\n")
                    f.write(char)
                    f.write("\n")
                
                else:
                    # end = num.index("]")
                    # print(end)
                    # new = num[0:end]
                    # print(new)

                    char = chr(int(num))
                    print(char, end="")
                    f.write(char)
                    # plain.append(char)
    # ===============================================

    # for option1
    # in Caeasr class
    # ===============================================


    # MAIN
    # used for the first time, when user didnt create an account yet
    # used one time per user
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
        
        selected_option = self.encryption_complexity()

        # create setup file
        with open("files/setup", mode="w") as w:
            w.write(f"{username}\n")
            w.write(f"{password}\n")
            w.write(f"{selected_option}\n")

        with open("files/key", mode="w") as ww:
            ww.write(f"{username[0]}\n")


        obj = Caesar()
        if selected_option == "1":
            # self.set_key(username[0])
            # encrypting setup file
            obj.encrypt_write("files/setup", "files/setup", username[0])

            # adding and encrypting to the accounts doc
            with open("temp_acc.txt", mode="w") as acc:
                acc.write("temp: [temp, data]")
            obj.encrypt_write("temp_acc.txt", "files/acc.txt", username[0])

            # removing temp file
            os.remove("temp_acc.txt")


        elif selected_option == "2":
            self.option2_ascii_encode("files/setup", "files/setup")

            with open("temp_acc.txt", mode="w") as acc:
                acc.write("temp: [temp, data]")
            self.option2_ascii_encode("temp_acc.txt", "files/acc.txt")
            # self.option2_ascii_decode("files/acc.txt", "temp")


        # not ready
        # elif selected_option == "3":
        #    fernet

        else:
            print("*error*")


        # removing temp file
        os.remove("temp_acc.txt")

        print("\n<process complete>\n")
    # ===============================================

    def login(self) -> None:
        alpha = "abcdefghijklmnopqrstuvwxyz"

        # title
        print("\nLOGIN")

        # decrypting
        with open("files/key", mode="r") as r:
            key = r.readlines()
        
        key_num = alpha.index(key[0].lower().strip("\n"))
        # print(key_num)


        obj = Caesar()
        obj.decrypt("files/setup", "files/temp_setup", key_num)


        # getting password
        with open("files/temp_setup", mode="r") as r:
        # with open("setup", mode="r") as r:
            lines = r.readlines()

        password = lines[1].strip("\n")
        # password = "testing"
        # print(password)

        # del
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

obj = Password()
# print(help(obj))

obj.account_setup()
# print(obj.encryption_complexity())

# if (not obj.check_if_account_exists()):
#     obj.account_setup()
# else:
#     print("Account already exists")
#     obj.login()

# obj.login()

# obj.password_master()
# obj.ascii_encode()
# obj.ascii_decode()
# ***************************************************c