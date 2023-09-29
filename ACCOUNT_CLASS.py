#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
    
    def print_info(self):
        print(self.account_number, self.balance)
        
    def change_balance(self, new_balance):
        self.balance += new_balance # denna tar både plus och minus.
        return self.balance
        
    def get_balance(self):
        return self.balance
        
    def __str__(self):
        return f"Account nr: {self.account_number}, Balance: {self.balance}"
    
    def __repr__(self):
        return f"account number = {self.account_number}, balance = {self.balance}"
    
    def make_dictionary_account(self):
        dictionary = {}
        dictionary["account_number"] = self.account_number
        dictionary["balance"] = self.balance
        return dictionary


# In[ ]:




