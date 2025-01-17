import time
# Import the Booking class from the booking package
from booking.booking import Booking

# The browser opened by selenium will be closed after the script finishes
# But there is a way to explicitly close it by using complex managers
with Booking() as bot:
    try:
        bot.land_first_page()
        time.sleep(2)
        bot.decline_cookies()
        bot.change_currency(currency="USD")
        bot.close_promo()
        bot.select_place_togo(place="New York")
        bot.select_dates(check_in_date="2025-01-18", check_out_date="2025-01-20")
        bot.select_adults(5)
        bot.click_search()
        bot.apply_filtration()
    except Exception as e:
        print(f"Unexpected error occurred during execution: Error: {e}")
