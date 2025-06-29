from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from prettytable import PrettyTable


class BookingReport:
    def __init__(self, driver):
        self.driver = driver

    def print_results(self):
        collection = []
        try:
            hotels = self.driver.find_elements(
                By.XPATH, ".//div[@data-testid='property-card']"
            )
            for hotel in hotels:
                hotel_name = hotel.find_element(
                    By.XPATH, ".//div[@data-testid='title']"
                ).text.strip()
                hotel_price = hotel.find_element(
                    By.XPATH, ".//span[@data-testid='price-and-discounted-price']"
                ).text.strip()
                hotel_score = hotel.find_element(
                    By.XPATH, ".//div[contains(@class, 'f63b14ab7a dff2e52086')]"
                ).text.split()
                collection.append(
                    [hotel_name, hotel_price, hotel_score[0]]
                )
            table = PrettyTable(
                field_names=["Hotel Name", "Price", "Score"]
            )
            table.add_rows(collection)
            print(table)
        except NoSuchElementException as error:
            print(f"Element not found while printing results: {error}")
        except Exception as error:
            print(f"Unexpected error while printing results: {error}")
