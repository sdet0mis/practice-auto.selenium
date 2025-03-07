from selenium.webdriver.common.by import By


class FormPageLocators:

    NAME_FIELD = (By.CSS_SELECTOR, "#name-input")
    PASSWORD_FIELD = (By.XPATH, "//input[@type='password']")
    MILK_CHECKBOX = (By.ID, "drink2")
    COFFEE_CHECKBOX = (By.ID, "drink3")
    YELLOW_RADIOBUTTON = (By.ID, "color3")
    DROPDOWN_LIST = (By.ID, "automation")
    AUTOMATION_TOOLS_LIST = (By.XPATH, "(//ul)[2]/li")
    EMAIL_FIELD = (By.CSS_SELECTOR, "#email")
    MESSAGE_FIELD = (By.XPATH, "//textarea[@name='message']")
    SUBMIT_BUTTON = (By.XPATH, "//button[@id='submit-btn']")
