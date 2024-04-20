#Controller.py

import Model

def input_name():
    name = input("Enter Name: ")
    return name

def input_password():
    password = input("Enter Password: ")
    return password

def login_controller(name, password):
    return Model.login_Model(name, password)
