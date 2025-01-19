# This file will include a class with instance methods
# That will be responsible to interact with our website
# After we have some results, to apply filtrations.
import time

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException

class BookingFiltrations:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def apply_star_rating(self, *star_ratings):
        retries = 3  # Number of retries to handle stale elements
        try:
            for attempt in range(retries):
                try:
                    # Locate the star filtration box
                    star_filtration_box = self.driver.find_element(By.XPATH, "//div[@data-filters-group='class']")

                    # Locate all child elements within the box
                    star_child_elements = star_filtration_box.find_elements(By.CSS_SELECTOR, "*")

                    for star_element in star_child_elements:
                        # Check if the star rating matches singular or plural forms
                        element_text = str(star_element.get_attribute("innerHTML")).strip()
                        if element_text in [f"{rating} star" if rating == 1 else f"{rating} stars" for rating in star_ratings]:
                            star_element.click()  # Click the desired star rating
                            print(f"Successfully clicked {element_text} filter.")
                    return
                except StaleElementReferenceException:
                    print(f"Stale element reference on attempt {attempt + 1}. Retrying...")
                    time.sleep(1)  # Short delay before retrying
                    continue  # Retry locating the elements
                except NoSuchElementException:
                    print("Star filtration box or child elements not found.")
                    return
                except Exception as e:
                    print(f"An error occurred: {e}")
                    return
            print(f"Failed to apply star filters after {retries} retries.")
        except Exception as e:
            print(f"Unexpected error occurred: {e}")

    def sort_price_lowest(self):
        sort_button = self.driver.find_element(By.CSS_SELECTOR, "button[data-testid='sorters-dropdown-trigger']")
        sort_button.click()
        price_lowest_option = self.driver.find_element(By.CSS_SELECTOR, "button[aria-label='Price (lowest first)']")
        price_lowest_option.click()

