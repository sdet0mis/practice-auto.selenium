import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select


class BasePage:

    @allure.step("Open browser")
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=10, poll_frequency=1)

    def find_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def fill_field(self, locator, data):
        return self.wait.until(EC.element_to_be_clickable(locator)).send_keys(
            data
        )

    def click(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator)).click()

    def click_by_js(self, locator):
        self.driver.execute_script(
            "arguments[0].click();",
            self.wait.until(EC.element_to_be_clickable(locator))
        )

    def select(self, locator):
        return Select(self.wait.until(EC.element_to_be_clickable(locator)))

    def get_alert(self):
        return self.wait.until(EC.alert_is_present())
