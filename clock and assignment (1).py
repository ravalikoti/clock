#!/usr/bin/env python
# coding: utf-8

# In[23]:


import tkinter as tk
from tkinter import font
import time

def update_clock():
    current_time = time.strftime("%H:%M:%S")
    label.config(text=current_time)
    label.after(1000, update_clock)

window = tk.Tk()
window.title("Digital Clock")

clock_font = font.Font(family="Arial", size=100, weight="bold")
label = tk.Label(window, font=clock_font, fg="blue", bg="white")
label.pack(padx=50, pady=20)

update_clock()
window.mainloop()


# In[1]:


get_ipython().system('pip install credentials')


# In[1]:


import requests

from_currency = str(
    input("Enter the currency you'd like to convert FROM: ")).upper()

to_currency = str(
    input("Enter in the currency you'd like to convert TO: ")).upper()

amount = float(input("Enter in the amount of money: "))

response = requests.get(
    f"https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}")

print(
    f"{amount} {from_currency} is {response.json()['rates'][to_currency]} {to_currency}")


# In[ ]:





# In[24]:


#Currency Converter

import requests
from tkinter import *
import tkinter as tk
from tkinter import ttk

class RealTimeCurrencyConverter():
    def __init__(self, url):
            self.data = requests.get(url).json()
            self.currencies = self.data['rates']

    def convert(self, from_currency, to_currency, amount): 
        initial_amount = amount 
        if from_currency != 'USD':
            amount = amount / self.currencies[from_currency] 
            amount = round(amount * self.currencies[to_currency], 4) 
        return amount

class App(tk.Tk):

    def __init__(self, converter):
        tk.Tk.__init__(self)
        self.title = ('Currency Converter')
        self.currency_converter = converter

        self.geometry("600x300")
        self.configure(bg="#B0E0E6")

        # Label
        self.intro_label = Label(self, text = 'Currency Convertor',  bg="#B0E0E6", fg = 'blue', justify = tk.CENTER)
        self.intro_label.config(font = ('Manrope',15,'bold'))
        self.intro_label.place(x = 40, y = 5)

        # Entry box
        valid = (self.register(self.restrictNumberOnly), '%d', '%P')
        self.amount_field = Entry(self, bd = 3, relief = tk.RIDGE, justify = tk.CENTER, validate='key', validatecommand=valid)
        self.converted_amount_field_label = Label(self, text = '', fg = 'black', bg = 'white', relief = tk.RIDGE, justify = tk.CENTER, width = 18, borderwidth = 3)

        # dropdown
        self.from_currency_variable = StringVar(self)
        self.from_currency_variable.set("INR") # default value
        self.to_currency_variable = StringVar(self)
        self.to_currency_variable.set("USD") # default value

        font = ("Manrope", 12, "bold")
        self.option_add('*TCombobox*Listbox.font', font)
        self.from_currency_dropdown = ttk.Combobox(self, textvariable=self.from_currency_variable, values=list(self.currency_converter.currencies.keys()), font = font, state = 'readonly', width = 15, justify = tk.CENTER)
        self.to_currency_dropdown = ttk.Combobox(self, textvariable=self.to_currency_variable, values=list(self.currency_converter.currencies.keys()), font = font, state = 'readonly', width = 13, justify = tk.CENTER)

        # placing
        self.from_currency_dropdown.place(x = 30, y= 120)
        self.amount_field.place(x = 30, y = 150)
        self.to_currency_dropdown.place(x = 340, y= 120)
        self.converted_amount_field_label.place(x = 340, y = 150)
        
        # Convert button
        self.convert_button = Button(self, text = "Convert", fg = "black", command = self.perform) 
        self.convert_button.config(font=('Manrope', 12, 'bold'))
        self.convert_button.place(x = 225, y = 135)

    def perform(self):
        amount = float(self.amount_field.get())
        from_curr = self.from_currency_variable.get()
        to_curr = self.to_currency_variable.get()

        converted_amount = self.currency_converter.convert(from_curr,to_curr,amount)
        converted_amount = round(converted_amount, 2)

        self.converted_amount_field_label.config(text = str(converted_amount))
    
    def restrictNumberOnly(self, action, string):
        regex = re.compile(r"[0-9,]*?(\.)?[0-9,]*$")
        result = regex.match(string)
        return string=="" or (string.count('.')<=1 and result is not None)

if __name__ == '__main__':
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    converter = RealTimeCurrencyConverter(url)
    App(converter)
    mainloop()


# In[ ]:





# In[ ]:




