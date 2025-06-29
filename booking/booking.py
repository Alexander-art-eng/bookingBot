import time
# Import webdriver from selenium
from selenium import webdriver
# Import the exceptions from selenium.common to handle exceptions
from selenium.common import WebDriverException, NoSuchElementException, TimeoutException
# Import the Service class from selenium.webdriver.chrome.service and alias it as ChromeService
from selenium.webdriver.chrome.service import Service as ChromeService
# Import the WebDriverWait class from selenium.webdriver.support.wait
from selenium.webdriver.support import expected_conditions as EC
# Import the WebDriverWait class from selenium.webdriver.support.wait
from selenium.webdriver.support.wait import WebDriverWait
# Import the ChromeDriverManager class from webdriver_manager.chrome
from webdriver_manager.chrome import ChromeDriverManager
# Import the By class from selenium.webdriver.common.by
from selenium.webdriver.common.by import By
# Import the constants module from the booking package
import booking.constants as const
# Import the BookingFiltrations class from the booking.booking_filtration module
from booking.booking_filtration import BookingFiltrations
# Import the BookingReport class from the booking.booking_report module
from booking.booking_report import BookingReport


# Define a class named Booking that inherits from webdriver.Chrome
class Booking(webdriver.Chrome):
    # Define the constructor method with a teardown parameter defaulting to True
    def __init__(self, teardown=True):
        # Create a ChromeService instance using ChromeDriverManager to install the ChromeDriver
        service = ChromeService(ChromeDriverManager().install())
        # Set the instance attribute teardown to the value of the teardown parameter
        self.teardown = teardown
        # To ingnore unnecessary errors from google drive (devTools logs)
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        # Call the constructor of the superclass (webdriver.Chrome) with the service parameter
        super(Booking, self).__init__(service=service, options=options)
        # Set the implicit wait time to 15 seconds to wait for elements to load
        self.implicitly_wait(15)
        # Maximize the browser window
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Check if teardown is True and the browser session is still active
        if self.teardown and self.session_id:
            # Prompt the user with a yes/no question to close the browser
            user_choice = input("Press any key to close the browser. ").strip().lower()
            # If the user types and key, close the browser
            self.quit()

    # Define a method named land_first_page that navigates to the base URL
    def land_first_page(self):
        # Use the get method to navigate to the URL specified in const.BASE_URL
        try:
            self.get(const.BASE_URL)
        except WebDriverException as error:
            print(f"Error navigating to {const.BASE_URL}: {error}")
            self.quit()

    # Define a method to decline the cookies in the webpage
    def decline_cookies(self):
        # Find the element with the id that it has
        try:
            decline_element = self.find_element(
                By.XPATH, ".//button[@id='onetrust-reject-all-handler']"
            )
            decline_element.click()
        except NoSuchElementException as error:
            print(f"cookies rejection button not found. Error: {error}")

    def change_currency(self, currency=None):
        try:
            currency_element = self.find_element(
                By.XPATH, ".//button[@data-testid='header-currency-picker-trigger']"
            )
            currency_element.click()
            currency_xpath = f"//button[@data-testid='selection-item']//div[contains(text(), '{currency}')]"
            selected_currency_element = WebDriverWait(self, 30).until(
                EC.element_to_be_clickable((By.XPATH, currency_xpath))
            )
            selected_currency_element.click()
        except TimeoutException as error:
            print(f"Timeout while changing currency to {currency}. Error: {error}")
        except NoSuchElementException as error:
            print(f"Currency element not found. Error: {error}")
        except Exception as error:
            print(f"Unexpected error while changing currency to {currency}. Error: {error}")

    # Define a method to close the promo banner
    def close_promo(self):
        try:
            promo_element_xpath = ".//div[contains(@class, 'fd1bba3c6c a5d282bede')]//button"
            promo_element = WebDriverWait(self, 10).until(
                EC.element_to_be_clickable((By.XPATH, promo_element_xpath))
            )
            promo_element.click()
        except TimeoutException as error:
            print(f"Timeout while closing promo banner. Error: {error}")
        except NoSuchElementException as error:
            print(f"The element to close the promo banner not found. Error: {error}")
        except Exception as error:
            print(f"Unexpected error while closing promo banner. Error: {error}")

    #  Define a method to select the place to go to
    def select_place_togo(self, place=None):
        try:
            search_element = self.find_element(
                By.XPATH, ".//div[contains(@class, 'be34ebee1c')]//input"
            )
            search_element.clear()
            search_element.send_keys(place)
            # selected_place_xpath = f"//li[@id='autocomplete-result-0']//div[contains(text(), '{place}')]"
            # selected_place_element = WebDriverWait(self, 10).until(
            #     EC.element_to_be_clickable((By.XPATH, selected_place_xpath))
            # )
            place_to_go = self.find_element(By.XPATH, f".//div[contains(@data-testid, 'autocomplete-result')]//div[contains(text(), '{place}')]")
            place_to_go.click()

        except NoSuchElementException as error:
            print(f"Search element not found. Error: {error}")
            return
        except Exception as error:
            print(f"Unexpected error while selecting the place to go to. Error: {error}")
            return

    # Define a method to select the check-in and check-out dates
    def select_dates(self, check_in_date=None, check_out_date=None):
        try:
            check_in_element = self.find_element(
                By.XPATH, f".//td[contains(@class, 'f6ec917956')]//span[@data-date='{check_in_date}']"
            )
            check_in_element.click()
            check_out_element = self.find_element(
                By.XPATH, f".//td[contains(@class, 'f6ec917956')]//span[@data-date='{check_out_date}']"
            )
            check_out_element.click()
        except NoSuchElementException as error:
            print(f"Check-in or check-out element not found. Error: {error}")
        except Exception as error:
            print(f"Unexpected error while selecting the check-in and check-out dates. Error: {error}")

    # Define a method to select the number of adults
    def select_adults(self, number_of_adults=1):
        try:
            adults_element = self.find_element(
                By.XPATH, ".//button[contains(@class, 'b3d1de1c28')]"
            )
            adults_element.click()

            while True:
                decrease_adults_element = self.find_element(By.XPATH, ".//div[contains(@class, 'e301a14002')]//button[contains(@class, 'aaf9b6e287 c857f39cb2')]")
                decrease_adults_element.click()
                adults_value = self.find_element(By.XPATH, ".//span[contains(@class, 'e32aa465fd')]").text
                if int(adults_value) == 1:
                    break

            increase_adults_element = self.find_element(By.XPATH, ".//button[contains(@class, 'aaf9b6e287 dc8366caa6')]")
            for _ in range(number_of_adults - 1):
                increase_adults_element.click()

        except NoSuchElementException as error:
            print(f"Adults element not found. Error: {error}")
        except Exception as error:
            print(f"Unexpected error while selecting the number of adults. Error: {error}")

    # Define a method to click the search button
    def click_search(self):
        try:
            search_button = WebDriverWait(self, 10).until(
                EC.element_to_be_clickable((By.XPATH, ".//button[contains(@class, 'a9d40b8d51')]/span"))
            )
            search_button.click()
        except NoSuchElementException as error:
            print(f"Search button not found. Error: {error}")
        except Exception as error:
            print(f"Unexpected error while clicking the search button. Error: {error}")

    # Define a method to apply the filtration
    def apply_filtration(self):
        try:
            filtration = BookingFiltrations(driver=self)
            filtration.apply_star_rating(1, 3, 5)
            time.sleep(1)
            filtration.sort_price_lowest()
        except NoSuchElementException as e:
            print(f"Element not found while applying filtration: {e}")
        except Exception as error:
            print(f"Error applying filtration: {error}")

    # Define a method to print a table of the results
    def show_results(self):
        results = BookingReport(driver=self)
        results.print_results()