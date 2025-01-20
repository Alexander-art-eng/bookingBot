BASE_URL = "https://www.booking.com"
import re

def validate_date(date_str):
    pattern = r"\d{4}-\d{2}-\d{2}"  # YYYY-MM-DD
    if re.match(pattern, date_str):
        return True
    print("Invalid date format. Please use YYYY-MM-DD.")
    return False

def validate_adults(adults):
    if adults.isdigit() and int(adults) > 0:
        return True
    print("Number of adults must be a positive integer.")
    return False

# Prompt user for inputs with validation
place_to_book = input("Where you want to go? ").strip()
while not place_to_book:
    print("Destination cannot be empty.")
    place_to_book = input("Where you want to go? ").strip()

check_in_date = input("What is the check in date? ")
while not validate_date(check_in_date):
    check_in_date = input("What is the check in date? ")

check_out_date = input("What is the check out date? ")
while not validate_date(check_out_date):
    check_out_date = input("What is the check out date? ")

adults = input("How many adults? ")
while not validate_adults(adults):
    adults = input("How many adults? ")

adults = int(adults)  # Convert to integer after validation