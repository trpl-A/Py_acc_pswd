class Caesar:
    """
    This class if used to read and encrypt, or decrypt the data from a text file
    It uses the Caesar cypher
    """

    def __init__(self):
        pass 

    # IF THE KEY IS KNOWN
    def decrypt(self, file_in="file_in", file_dest="data", key=1) -> None:
        # reading text file
        file = open(f"{file_in}", "r")
        l = file.readlines()
        # print(len(l))


        # removing \n 
        s = []
        for i in l:
            # i = i[0:-2]
            i = i.replace("\n", "")
            if i == "":
                pass 

            else:
                s.append(i)


        # writing potential message to a text file
        p_msg = open(f"{file_dest}", "a")
        # p_msg = open(f"{file_dest}", "w")

        # decoding
        alpha = "abcdefghijklmnopqrstuvwxyz"
        # alpha_u = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        for m in s:
            for n in m:
                if n not in alpha:
                    # print(n, end="")
                    p_msg.write(n)

                else:
                    lttr = (alpha.index(n) + (26 - key)) % 26
                    a = alpha[lttr]
                    # print(a, end="")
                    p_msg.write(a)
            # print()
            p_msg.write("\n")

        # print("\n<decoding complete>")
    # =============================================

        
    def encrypt(self, filename, key) -> None:
        file = open(filename, "r")
        lines = file.readlines()
        # print(lines)

        alpha_u = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        alpha_l = "abcdefghijklmnopqrstuvwxyz"

        # key 
        k = ""
        if key in alpha_u:
            k = alpha_u.index(key)
            print(k)
        
        elif key in alpha_l:
            k = alpha_l.index(key)


        # encryption
        num_format = []
        for line in lines:
            # replacing \n 
            line.replace("\n", "*")

            # converting letters to their index in the alphabet
            for char in line:
                if char in alpha_l:
                    char = (alpha_l.index(char) + int(k)) % 26
                    num_format.append(char)
                    # print(char, end="")

                elif char in alpha_u:
                    char = (alpha_u.index(char) + int(k)) % 26
                    num_format.append(char)
                    # print(char, end="")

                else:
                    num_format.append(char)
                    # print(char)

        # print(num_format)


        # converting (indexes) numbers to letters
        msg = ""
        nums = range(0, 26)
        for n in num_format:
            if n not in nums:
                letter = str(n)
                # print(letter, end="")

            elif n == "*":
                print()
                
            else:
                letter = alpha_l[n]
                # print(letter, end="")


            msg += letter

        # writing to file
        # with open("eee.txt", "w") as w:
        #     w.write(msg)

        # print("\n<Encryption complete>")
        return msg 
    # =============================================

    def encrypt_write(self, input_file="test.txt", dest_file="new_encoded.txt", key="m") -> None:
        encrypting_data = self.encrypt(input_file, key)
        # print(encrypting_data)

        # writing to text file
        file = open(f"{dest_file}", "w")
        file.write(f"{encrypting_data}")
    # =============================================

# *************************************************

# obj = Caesar()
# print(obj.__doc__)
# print(help(obj))

# a.decrypt(file, 12)

# in_file = "data_encoded.txt"
# dest_file = "dest.txt"
# a.encrypt_write()
# *************************************************