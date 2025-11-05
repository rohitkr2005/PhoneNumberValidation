import phonenumbers
from phonenumbers import geocoder, carrier, timezone

try:
    
    phone_number_str = input("Enter phone number with country code (e.g., +91XXXXXXXXXX): ")

    # 1. Parse the number
    parsed_number = phonenumbers.parse(phone_number_str)

    # 2. Get the country/region (geocoder)
    # Note: This is the general region, not a specific address
    region = geocoder.description_for_number(parsed_number, "en")

    # 3. Get the carrier
    service_provider = carrier.name_for_number(parsed_number, "en")

    # 4. Get the time zone
    time_zones = timezone.time_zones_for_number(parsed_number)

    # Print the results
    print(f"--- Information for {phone_number_str} ---")
    print(f"Valid Number: {phonenumbers.is_valid_number(parsed_number)}")
    print(f"General Region: {region}")
    print(f"Carrier: {service_provider}")
    print(f"Time Zones: {time_zones}")

except phonenumbers.phonenumberutil.NumberParseException as e:
    print(f"Error: {e}. Please enter a valid number with a country code (e.g., +91).")