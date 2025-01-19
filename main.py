import time
# Import the Booking class from the booking package
from booking.booking import Booking
from booking.constants import place_to_book, check_in_date, check_out_date, adults

# The browser opened by selenium will be closed after the script finishes
# But there is a way to explicitly close it by using complex managers
with Booking() as bot:
    try:
        bot.land_first_page()
        time.sleep(2)
        bot.decline_cookies()
        bot.change_currency(currency="USD")
        bot.close_promo()
        bot.select_place_togo(place=place_to_book)
        bot.select_dates(check_in_date=check_in_date, check_out_date=check_out_date)
        bot.select_adults(number_of_adults=adults)
        bot.click_search()
        bot.apply_filtration()
        bot.show_results()
    except Exception as e:
        print(f"Unexpected error occurred during execution: Error: {e}")
