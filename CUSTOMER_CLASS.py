#!/usr/bin/env python
# coding: utf-8

# In[4]:
from ACCOUNT_CLASS import *

class Customer:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.account_list = []
        self.account_number = 1
        
    def print_info(self):
        print(self.username, self.account_list)
        
    def check_password(self, password):
        if self.password == password:
            return True
        return False
        
    def add_account(self, balance):
        self.account_list.append(Account(self.account_number, balance))
        print("Account added.")
        self.account_number += 1
        
    def __str__(self):
        return f"{self.username}, {self.password}"
    
    def __repr__(self):
        return f"username = {self.username}, password = {self.password}"
    
    def make_dictionary_customer(self):
        dictionary = {}
        dictionary["username"] = self.username
        dictionary["password"] = self.password
        dictionary["account_list"] = []
        for account in self.account_list:
            dictionary["account_list"].append(account.make_dictionary_account())
        return dictionary


# In[ ]:





# In[ ]:




