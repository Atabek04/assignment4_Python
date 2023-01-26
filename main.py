import json
import pygame

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

pygame.init()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F1:
                data = get_login_and_password()
                save_to_file(data)
            elif event.key == pygame.K_F2:
                print("F2 pressed.")
            elif event.key == pygame.K_F3:
                print("F3 pressed.")
            else:
                print("Invalid function key.")
