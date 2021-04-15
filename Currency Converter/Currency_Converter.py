from forex_python.converter import CurrencyRates

current_rate = CurrencyRates()
amount = int(input("Enter the amount : "))
from_currency = input("From Currency : ").upper()
to_currency = input("To Currency : ").upper()
result = current_rate.convert(from_currency,to_currency,amount)
print(amount,from_currency,"to",to_currency,"=",result)