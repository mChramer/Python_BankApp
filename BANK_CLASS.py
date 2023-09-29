#!/usr/bin/env python
# coding: utf-8

# In[1]:

from ACCOUNT_CLASS import *
from CUSTOMER_CLASS import *

import json

class Bank:
    def __init__(self, bank_name):
        self.bank_name = bank_name
        self.customer_list = []
        self.current_customer = None # variabel för att se om kunden är inloggad.
        self.bank_dictionary_list = []
        
    def online(self):
        if self.current_customer != None:
            return True
        return False
    
    def get_customers(self):
        for customer in self.customer_list:
            print(f"Username: {customer.username}, password: {customer.password}")
        
    def add_customer(self, username, password):
        self.customer_list.append(Customer(username, password))
        
    def get_customer(self, sought_username): # hämta specifik kund via användarnamn.
        for customer in self.customer_list:
            if customer.username == sought_username:
                return customer
        return False
    
    def change_customer_password(self, username, new_password):
        for customer in self.customer_list:
            if customer.username == username:
                customer.password = new_password
                print("Password changed.")
                return customer
        return False
    
    def remove_customer(self, username):
        for customer in self.customer_list:
            if customer.username == username:
                self.customer_list.remove(customer)
                print("Customer removed.")
        
    def login (self, username, password):
        for user in self.customer_list:
            if username == user.username and password == user.password:
                self.current_customer = user
                return True
        return False
        
    def logout (self):
        self.current_customer = None
        return True
        
    def get_accounts(self):  # hämta alla konton som tillhör användaren som är inloggad.
        if self.online() == True:
            return self.get_customer(self.current_customer.username).account_list
        
        # RETURN: använder funktionen get_customer för att hitta kunden, sedan letar vi upp current_customer.username för 
        # att få fram username på den som är inloggad. punkt.account_list ger oss listan på den inloggade kundens accounts.    
        # bank.customer_list[0].account_list - account_list är en lista i listan customer_list som tillhör spec. kund.
          
    def add_account(self, balance=0): # lägger till ett konto till den inloggade kunden.
        if self.online() == True:
            return self.current_customer.add_account(balance)
        
    def remove_account(self, account_number): # ta bort ett konto från den inloggade kunden.
        if self.online() == True:
            #for customer in self.customer_list:
                for account in self.current_customer.account_list:
                    if account.account_number == account_number:
                        self.current_customer.account_list.remove(account)
                        return True
        return False
        
        
    def get_account(self, account_number): # hämta ett konto från användaren som är inloggad.
        if self.online() == True:
            for account in self.current_customer.account_list:
                if account.account_number == account_number:
                    return account #.get_balance() när denna biten är med ges endast saldot.
        return False
        
    def deposit(self, account_number, amount):
        if amount < 0:
            print("It can't be a negative number.")
            return
        if self.online() == True:
            for account in self.current_customer.account_list:
                if account.account_number == account_number:
                    account.change_balance(amount)
                    print("Deposit succeeded!")
                    return
        print(f"Account with number {account_number} not found.")
                      
                
    def withdraw(self, account_number, amount):
        if amount < 0:
            print("It can't be a negative number.")
            return
        if self.online() == True:
            for account in self.current_customer.account_list:
                if account.account_number == account_number:
                    if account.balance < amount:
                        print("Insufficient funds.")
                        return
                    account.change_balance(-amount)
                    print("Withdraw succeeded!")
                    return
        print(f"Account with number {account_number} not found.")
        
    def save_customer(self):
        #with open("bank.json", "w") as file:
        file = open("bank.json", "w")
        for customer in self.customer_list:
            self.bank_dictionary_list.append(customer.make_dictionary_customer())
        json_string = json.dumps(self.bank_dictionary_list, indent=2)
        file.write(json_string)
        file.close()
        self.customer_list.clear()
        self.bank_dictionary_list.clear()
        
        
    def load_customer(self):
        self.customer_list.clear()
        with open("bank.json", "r") as file:
            dictionary = json.load(file)
        for customer_dictionary in dictionary:
            customer = Customer(customer_dictionary["username"], customer_dictionary["password"])
            self.customer_list.append(customer)
            for account_dictionary in customer_dictionary["account_list"]:
                account = Account(account_dictionary["account_number"], account_dictionary["balance"])
                customer.account_list.append(account)
        for customer in self.customer_list:
            print(f"Customer: {customer.username}, Password: {customer.password}")
            for account in customer.account_list:
                print(f"Account: {account.account_number}, Balance: {account.balance}")
        file.close()


# In[ ]:




