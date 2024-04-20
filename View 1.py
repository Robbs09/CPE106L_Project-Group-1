#View.py

import Controller

def login_View():
    print("-----------Login--------------\n")
    
    name = Controller.input_name()
    password = Controller.input_password()

    if Controller.login_controller(name, password):
        print("Login Successful!")
    else:
        print("Invalid Username/Password")

# Call the login_View function
login_View()
