# Please use your country code
# For example, if you are from US, please use +1, or Nigeria +234
# For more information, please visit https://en.wikipedia.org/wiki/List_of_country_calling_codes

import phonenumbers
from phonenumbers import timezone, geocoder, carrier

def get_phone_number_details(phone_number):
    try:
        phone = phonenumbers.parse(phone_number)
        time_zones = timezone.time_zones_for_number(phone)
        carrier_name = carrier.name_for_number(phone, "en")
        region = geocoder.description_for_number(phone, "en")
        return phone, time_zones, carrier_name, region
    except phonenumbers.phonenumberutil.NumberParseException:
        return None, None, None, None

def main():
    phone_number = input("Enter your phone number: ")
    phone, time_zones, carrier_name, region = get_phone_number_details(phone_number)
    
    if phone:
        print(f'Phone number: {phone}')
        print(f'Time zones: {time_zones}')
        print(f'Carrier: {carrier_name}')
        print(f'Region: {region}')
    else:
        print("Invalid phone number. Please try again with the correct format.")

if __name__ == "__main__":
    main()
