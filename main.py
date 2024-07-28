
import requests 
import json
from datetime import datetime
import time
import sys

class CurrencyConverter:
    def __init__(self): 
        while True:
            try:
                self.currencies=self.load_currency_data()
                break
            except:
                self.currencies_data=self.fetch_currency_data()
            
                self.json_data=self.response_info
                with open('json_data','w') as f: #serialization
                     json.dump(self.json_data, f)
                break
            else:
                break
        return 
    
    def fetch_currency_data(self):
       
        # Use this code to fetch currency data from openexchangerates.org.
        app_id = "a6350f40e9f74a86afc4b0b8199f4f79" # Add app_id from openexchangerates.org 
        url = f"https://openexchangerates.org/api/latest.json?app_id={app_id}"
        headers = {"accept": "application/json"} # This needs to be added, it tells the API that they should return JSON
        response = requests.get(url, headers=headers)
        print(f"Status code: {response.status_code}") #status code if the request was successful(200)
        self.response_info = response.json()#Store API response 
              
        return self.response_info
       
        
    
    def convert_from_usd(self):
        
        #self.to_currency = to_currency
        with open('json_data', 'r') as read_it: #deserialization
            self.read_it = json.load(read_it)
        self.base = self.read_it['base']
        self.rates=self.read_it['rates'] 

        while True:
            self.to_currency= input("Currency to convert to: ").upper()
            if self.to_currency in self.rates:
                break
            else:
                print('Type error! Enter correct 3 letter code')
                continue
        while True:
            try:
                amount = float(input("Amount: "))
            except ValueError:
                print('Type error! Enter only figures')
                continue
            else:
                break    
         
        for currency, rate in self.rates.items():
          if currency == self.to_currency:
            conversion = rate * amount
            print("1", self.read_it['base'], "=", currency, rate)
            print(f"{amount} {self.read_it['base']} = {currency} {round(conversion,2)}") 
           
        return       
        
            
    def convert_any_currency(self):
        
        self.rates=self.read_it['rates']
        print(f'Enter 3 letter code of curruncies.')
        while True:
            
            from_currency=input("From currency: ").upper()
            if from_currency in self.rates:
                break
            else:
                print('Type error! Enter correct 3 letter code')
                continue
        while True:
            to_currency=input("To currency: ").upper()
            if to_currency in self.rates:
                break
            else:
                print('Type error! Enter correct 3 letter code')
                continue
        while True:
            try:
                initial_amount = float(input("Amount: "))
            except ValueError:
                print('Type error! Enter only figures')
                continue
            else:
                break     
                
        if from_currency != 'USD':
            amount = initial_amount/self.rates[from_currency]
            #print(amount,from_currency,'is equivalent to', self.read_it['base'])
            for currency, rate in self.rates.items():
                if currency == to_currency:
                    conversion = rate * amount
                    print(f"{from_currency} {initial_amount}  = {currency} {round(conversion,2)}")
        return
    
    def list_currencies(self):#is ther a better way to list currencies without dictionary
        
        self.data = self.load_currency_data()
        print("\nCurrency list:")
        print(f"Base currency: {self.read_it['base']}")
        print(f"Timestamp: {self.read_it['timestamp']}") 
                
        self.rates=self.read_it['rates'] 
        print(self.rates.keys())
               
        return 

    
    def load_currency_data(self):
       
        with open('json_data', 'r') as read_it: #deserialization
            self.read_it = json.load(read_it)
        timestamp = self.read_it['timestamp']
        current_time = time.time()
        diff= current_time -timestamp
        if diff > 3600:
            json_data=self.response_info
            with open('json_data','w') as f: #serialization
                json.dump(json_data, f)
                print('Older json data updated now')
                    
        else:
            print('Jason data upto date!')

    def export_to_json(self):
        
        print(f'Json data exported and updated!')
        self.export = self.fetch_currency_data()
        self.json_data=self.response_info
        
        with open('json_data', 'w') as f:
            json.dump(self.json_data, f)       
       
        return 
           
             
    
def main():
        
    C = CurrencyConverter()

    while True:
        print(f'\nWhat would you like to do?')
        print(f'    [0] - (G) List all currencies')
        print(f'    [1] - (G) Convert USD to a currency of choice')
        print(f'    [2] - (G) Refresh the data (fetch new currency data, this is because the API updates new currency rates every hour)')
        print(f'    [3] - (G) Export the data to JSON')
        print(f'    [4] - (VG) Convert from any currency to any currency that is available on the API')
        print(f'    [q] - Quit')

        user_input=input()
        if user_input == 'q':
            sys.exit()
       
        elif user_input == '0':
            C.list_currencies()
            continue


        elif user_input == '1':
            C.convert_from_usd()
            continue
            
            
        elif user_input == '2':
            C.load_currency_data()
            continue 
        
        elif user_input == '3':
            C.export_to_json()
            continue

        elif user_input == '4':
            C.convert_any_currency()
            continue
        else:
            print('Tye Error! Please choose from the list.')
            continue
        
    return        
        
if __name__ == "__main__":   
    
    main()