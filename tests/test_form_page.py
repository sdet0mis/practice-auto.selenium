import random

import allure
import pytest
from faker import Faker

from pages.form_page import FormPage

fake = Faker()


@allure.title("Test form page")
@allure.severity(allure.severity_level.BLOCKER)
@pytest.mark.smoke
def test_form_page(driver):
    form_page = FormPage(driver)
    form_page.open_form_page()
    form_page.enter_name(fake.name())
    form_page.enter_password(fake.password())
    form_page.click_milk_checkbox()
    form_page.click_coffee_checkbox()
    form_page.click_yellow_radiobutton()
    form_page.select_dropdown_list(random.choice(("yes", "no", "undecided")))
    form_page.enter_email(fake.email())
    tools = [tool.text for tool in form_page.get_automation_tools()]
    form_page.enter_message(f"{len(tools)} {max(tools, key=len)}")
    alert = form_page.click_submit_button()
    assert alert.text == "Message received!"
