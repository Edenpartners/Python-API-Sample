"""
    Eden Client API Samples
"""
from eden_client_api.api import EdenClientApi as eden

""" 
    initialize
"""
api = eden(eden.EDEN_PROTOTYPE_NETWORK)
token = ''

""" 
    user authenticate before starting.
"""
def authenticate_user():
    id = input("Please input your id : ")
    pwd = input("Please input your password : ")    
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
    else:
        return False
    
    return True


if __name__ == '__main__':
    if authenticate_user():
        while run_api_test():
            pass    
    else:
        print("Authenticate failed")