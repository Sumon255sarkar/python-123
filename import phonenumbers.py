import phonenumbers
from phonenumbers import geocoder

# Parsing phone numbers
phone_number1 = phonenumbers.parse("+881712634782", "BD")
phone_number2 = phonenumbers.parse("+918878586271", "IN")
phone_number3 = phonenumbers.parse("+12136574920", "US")
phone_number4 = phonenumbers.parse("+201234567890", "EG")

# Displaying the location of the phone numbers
print("\nPhone Numbers Location\n")
print(geocoder.description_for_number(phone_number1, "en"))
print(geocoder.description_for_number(phone_number2, "en"))
print(geocoder.description_for_number(phone_number3, "en"))
print(geocoder.description_for_number(phone_number4, "en"))
