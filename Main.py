"""
Started:    01.01.23
Updated:    15.11.23
Developer:  trpl-A
"""

import os 
from Password import Password
# -----------------------------------


def main():
    """
    The class containing the main function/method for this program.
    """

    obj1 = Password()

    # check if files dir exists
    obj1.check_if_dir_exists()

    # checking if account exists
    if (not obj1.check_if_account_exists()):
        # print(False)
        obj1.account_setup()
    else:
        # print("Account already exists")
        os.system("cls")
        obj1.login()
# ========================================

if __name__ == "__main__":
    main()
    os.system("attrib +h files" )
    print("\n<END OF PROGRAM>")
# ========================================