#Model.py

import csv

def login_Model(name, password):
    with open("Accounts.csv", 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            if row[0] == name and row[1] == password:
                return True
    return False  # Return False if no matching account is found
