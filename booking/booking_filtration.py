# This file will include a class with instance methods
# That will be responsible to interact with our website
# After we have some results, to apply filtration.
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class BookingFiltrations:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def apply_star_rating(self, *star_ratings: int):
        try:
            # Locate the star filtration box
            star_container = self.driver.find_element(By.XPATH, ".//div[@id='filter_group_class_:R9uqcnr5:']")
            stars = self.driver.find_elements(star_container,
                                              ".//div[@data-testid='filters-group-label-container']//div")
            for star in stars:
                star_text = star.get_attribute("innerHTML").strip()
                if star_text in [f"{rating} star" if rating == 1 else f"{rating} stars" for rating in star_ratings]:
                    star.click()
                    print(f"Success in clicking {star_text} filter.")
        except NoSuchElementException:
            print("Star filtration box or child elements not found.")
            return
        except Exception as e:
            print(f"An error occurred during star filtration: {e}")
            return

    def sort_price_lowest(self):
        try:
            sort_button = self.driver.find_element(By.XPATH, ".//button[@data-testid='sorters-dropdown-trigger']")
            sort_button.click()
            price_lowest_option = self.driver.find_element(By.CSS_SELECTOR, ".//button[@data-id='price']")
            price_lowest_option.click()
        except NoSuchElementException as e:
            print(f"Sort button or price lowest option not found. Error: {e}")
