import hashlib
from util import *
def main():
    # user_name=input("enter user name: ")
    # user_password=input("enter user password ")
    # encrypt_pwd=hashlib.md5(user_password.encode()).hexdigest()
    user_input({"name":"Rafal","pwd":"Rafal90"})
    user_input({"name":"Lara","pwd":"laly34"})

    res_data=encrypt_data()
    print(res_data)
main()