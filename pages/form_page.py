import allure

from pages.base_page import BasePage
from config.urls import URLs
from config.locators import FormPageLocators


class FormPage(BasePage):

    @allure.step("Open form page")
    def open_form_page(self):
        self.driver.get(URLs.FORM_PAGE)

    @allure.step("Enter name")
    def enter_name(self, name):
        self.fill_field(FormPageLocators.NAME_FIELD, name)

    @allure.step("Enter password")
    def enter_password(self, password):
        self.fill_field(FormPageLocators.PASSWORD_FIELD, password)

    @allure.step("Click milk checkbox")
    def click_milk_checkbox(self):
        self.click(FormPageLocators.MILK_CHECKBOX)

    @allure.step("Click coffee checkbox")
    def click_coffee_checkbox(self):
        self.click(FormPageLocators.COFFEE_CHECKBOX)

    @allure.step("Click yellow radiobutton")
    def click_yellow_radiobutton(self):
        self.click(FormPageLocators.YELLOW_RADIOBUTTON)

    @allure.step("Select dropdown list")
    def select_dropdown_list(self, value):
        self.select(FormPageLocators.DROPDOWN_LIST).select_by_value(value)

    def get_automation_tools(self):
        return self.find_elements(FormPageLocators.AUTOMATION_TOOLS_LIST)

    @allure.step("Enter email")
    def enter_email(self, email):
        self.fill_field(FormPageLocators.EMAIL_FIELD, email)

    @allure.step("Enter message")
    def enter_message(self, message):
        self.fill_field(FormPageLocators.MESSAGE_FIELD, message)

    @allure.step("Click submit button")
    def click_submit_button(self):
        self.click_by_js(FormPageLocators.SUBMIT_BUTTON)
        return self.get_alert()
