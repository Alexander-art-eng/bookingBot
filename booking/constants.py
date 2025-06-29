import re

REGEXP_DATE_FORMAT = re.compile(r"\d{4}-\d{2}-\d{2}") # YYYY-MM-DD
BASE_URL = "https://www.booking.com"


def validate_date(check_dates: str) -> bool:
    return True if REGEXP_DATE_FORMAT.match(check_dates) else False

def validate_adults(adults_num: int) -> bool:
    return True if adults_num > 0 else False

# Prompt user for inputs with validation
place_to_book = input("Where you want to go? ").capitalize()
while not place_to_book:
    print("Destination cannot be empty.")
    place_to_book = input("Where you want to go? ")

check_in_date = input("What is the check in date? ")
while not validate_date(check_in_date):
    check_in_date = input("What is the check in date? ")

check_out_date = input("What is the check out date? ")
while not validate_date(check_out_date):
    check_out_date = input("What is the check out date? ")

adults = int(input("How many adults? "))
while not validate_adults(adults):
    adults = input("How many adults? ")
