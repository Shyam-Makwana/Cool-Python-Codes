import phonenumbers

# geocoder: to know the specific
# location to that phone number
from phonenumbers import geocoder
from phonenumbers import carrier

# Indian phone number example: +91**********
phone_number = phonenumbers.parse("+91**********")
	
# this will print the country name
print(geocoder.description_for_number(phone_number,'en'))

# this will print the service provider name
print(carrier.name_for_number(phone_number,'en')) 

