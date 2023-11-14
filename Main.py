"""
Started:    01.01.23
Updated:    07.11.23
Developer:  trpl-A
"""

import os 
from Password import Password


def main():
    obj1 = Password()

    # show 
    # os.system("attrib +h files" )

    # checking if account exists
    if (not obj1.check_if_account_exists1()):
        print(False)
        obj1.account_setup()
    else:
        # print("Account already exists")
        os.system("cls")
        obj1.login()

    # # hidding file
    os.system("attrib +h files" )
# ========================================

if __name__ == "__main__":
    main()
    # os.system("attrib -h data_encoded.txt" )
    print("\n<END OF PROGRAM>")
# ========================================