import json
import msvcrt
# import getch

def get_login_and_password():
    login = input("Enter login: ")
    password = input("Enter password: ")

    # Check if login and password contain only symbolic and numeric values
    if not all(c.isalnum() for c in login + password):
        raise ValueError("You must enter only symbolic and numeric values!")

    return {'login': login, 'password': password}

def save_to_file(data):
    with open('credentials.txt', 'w') as f:
        json.dump(data, f)
    print("Credentials saved to file.")

def check_function_key():
    key = ord(msvcrt.getch())
    if key == 59:
        data = get_login_and_password()
        save_to_file(data)
    elif key == 60:
        print("F2 pressed.")
    elif key == 61:
        print("F3 pressed.")
    else:
        print("Invalid function key.")

while True:
    check_function_key()
