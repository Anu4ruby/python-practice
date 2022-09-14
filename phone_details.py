#https://www.geeksforgeeks.org/get-phone-number-information-using-python/
#pip install phonenumbers
import phonenumbers

# geocoder: to know the specific
# location to that phone number
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier

phone_number = input("enter the phone number with area code-  " )
phone_number = phonenumbers.parse(phone_number)
# Indian phone number example: +91**********
# Nepali phone number example: +977**********

# this will print the country name
print("Location ",geocoder.description_for_number(phone_number,
									'en'))

# this will print the service provider name
print("Carrier name",carrier.name_for_number(phone_number,
                              'en'))
