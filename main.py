# Please use your country code
# For example, if you are from US, please use +1, or Nigeria +234
# For more information, please visit https://en.wikipedia.org/wiki/List_of_country_calling_codes

from time import time
from numpy import number
import phonenumbers
from phonenumbers import timezone, geocoder, carrier
number = input("Enter your phone number: ")
phone = phonenumbers.parse(number)
time = timezone.time_zones_for_number(phone)
car = carrier.name_for_number(phone, "en")
reg = geocoder.description_for_number(phone, "en")

print(f'Phone number: {phone}')
print(f'Time: {time}')
print(f'Carrier: {car}')
print(f'Reg: {reg}')
