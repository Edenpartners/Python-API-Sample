"""
    Eden Client API Samples
"""
from eden_client_api.api import EdenClientApi as eden
import getpass

""" 
    initialize
"""
api = eden(eden.EDENCHAIN_BETA_RELEASE)
token = ''

""" 
    user authenticate before starting.
"""
def authenticate_user():
    id = input("Please input your id : ")
    pwd = getpass.getpass("Please input your password : ")    
    global token
    token = api.authenticate_user(id,pwd)

    if token != '':
        return True
    else:
        return False

def show_menu():
    print("--------------------------")
    print(" 1. Get User Balance")
    print(" 2. Get User information")
    print(" 3. Get Coin Address")
    print(" 4. Get User Transaction")
    print(" 5. Add Eth Address")
    print(" 6. Del Eth Address")
    print(" 7. Deposit Token")
    print(" 8. Withdraw Token")
    print("--------------------------")
    print(" Other menu will quit this program")

def run_api_test():
    show_menu()
    key_value = input("Please select from menu : ")

    if key_value == '1':
        print(api.get_user_balance(token))
    elif key_value == '2':
        print(api.get_user_info(token))
    elif key_value == '3':
        print(api.get_coin_server_address(token))
    elif key_value == '4':
        print(api.get_user_transaction(token,1,10))
    elif key_value == '5':
        priv = input("Enter your ethereum privat key : ")
        ret = api.add_eth_address(token, priv)
        if ret:
            print("Add Success")
        else:
            print("Add Failed")
    elif key_value == '6':
        priv = input("Enter your ethereum privat key : ")
        ret = api.del_eth_address(token, priv)
        if ret:
            print("Del Success")
        else:
            print("Del Failed")
    elif key_value == '7':
        hash = input("Enter Ethereum Transaction Hash : ")
        ret = api.deposit_token(token,hash)
        if ret:
            print("Deposit Success")
        else:
            print("Deposit Failed")
    elif key_value == '8':
        addr = input("Enter Ethereum Address : ")
        amount = input("Enter Token amount to withdraw : ")
        ret = api.withdraw_token(token,addr,amount)
        if ret:
            print("Withdraw Success : txhash - " + ret)
        else:
            print("Withdraw Failed")
    else:
        return False
    
    return True


if __name__ == '__main__':
    if authenticate_user():
        while run_api_test():
            pass    
    else:
        print("Authenticate failed")
