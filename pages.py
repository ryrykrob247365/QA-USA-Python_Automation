import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import data
from helpers import retrieve_phone_code

class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    call_taxi_button = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[1]/div[3]/div[1]/button')
    supportive_icon = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[1]/div[5]/div[2]')
    active_plan_card = (By.XPATH, '//div[@class="tcard active"]//div[@class="tcard-title"]')
    supportive_plan_card = (By.XPATH, '//div[contains(text(), "Supportive")]')
    supportive_plan_card_parent = (By.XPATH, '//div[contains(text(), "Supportive")]//..')
    payment_method = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[2]/div[2]/div[3]/img')
    new_card = (By.XPATH, '//div[contains(text(), "Add card")]')
    fill_info = (By.ID, 'number')
    fill_code = (By.XPATH, '//input[@class="card-input" and @id="code"]')
    empty_area = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/form/div[3]')
    select_link = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/form/div[3]/button[1]')
    current_payment_method = (By.CLASS_NAME, 'pp-value-text')
    make_message = (By.XPATH, '//*[@id="comment"]')
    blankets_handkerchiefs = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div[2]')
    blankets_checked = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div[2]/div/input')
    plus_ice_cream = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[3]')
    more_ice_cream = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[2]')
    order_taxi_button = (By.CLASS_NAME, 'smart-button')
    new_car_search = (By.XPATH, '//div[text() = "Car search"]')
    type_phone_number = (By.XPATH, '//div[text() = "Phone number"]')
    phone_number = (By.CLASS_NAME, 'np-text')
    typing_number = (By.ID, 'phone')
    phone_next_button = (By.CSS_SELECTOR, '.full')
    phone_code = (By.ID, 'code')
    phone_confirm_button = (By.XPATH, '//button[contains(text(), "Confirm")]')
    close_button_payment_method = (
        By.XPATH, '//div[@class="payment-picker open"]//button[@class="close-button section-close"]')

    def __init__(self, driver):
        self.driver = driver

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_route(self, from_address, to_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)
        self.driver.find_element(*self.to_field).send_keys(to_address)
        self.driver.find_element(*self.call_taxi_button).click()

    def select_supportive_plan(self):
        """ Here we need to check that the Supportive tariff is not selected.
         If it is already selected, there is no extra click and the test class runs smoothly"""
        if self.driver.find_element(*self.supportive_plan_card_parent).get_attribute("class") != "tcard active":
            card = WebDriverWait(self.driver, 3).until(
                expected_conditions.visibility_of_element_located(self.supportive_plan_card))
            self.driver.execute_script("arguments[0].scrollIntoView();", card)
            card.click()

    def get_current_selected_plan(self):
        return self.driver.find_element(*self.active_plan_card).text

    def add_new_card(self, card_number, security_code):
        self.driver.find_element(*self.payment_method).click()
        time.sleep(2)
        self.driver.find_element(*self.new_card).click()
        self.driver.find_element(*self.fill_info).send_keys(card_number)
        self.driver.find_element(*self.fill_code).send_keys(security_code)
        self.driver.find_element(*self.empty_area).click()
        self.driver.find_element(*self.select_link).click()
        self.driver.find_element(*self.close_button_payment_method).click()

    def get_current_payment_method(self):
        return self.driver.find_element(*self.current_payment_method).text

    def enter_comment(self, type_message):
        self.driver.find_element(*self.make_message).send_keys(type_message)

    def get_comment(self):
        return self.driver.find_element(*self.make_message).get_attribute('value')

    def select_blankets(self):
        self.driver.find_element(*self.blankets_handkerchiefs).click()

    def get_blankets_and_handkerchiefs(self):
        return self.driver.find_element(*self.blankets_checked).get_attribute('checked')

    def add_ice_cream(self):
        self.driver.find_element(*self.plus_ice_cream).click()

    def get_plus_ice_cream(self):
        return self.driver.find_element(*self.more_ice_cream).text

    def order_taxi(self):
        self.driver.find_element(*self.order_taxi_button).click()

    def car_search_displayed(self):
        return self.driver.find_element(*self.new_car_search).is_displayed()

    def use_phone_number(self):
        self.driver.find_element(*self.type_phone_number).click()
        self.driver.find_element(*self.typing_number).send_keys(data.PHONE_NUMBER)
        self.driver.find_element(*self.phone_next_button).click()
        time.sleep(3)
        self.driver.find_element(*self.phone_code).send_keys(retrieve_phone_code(self.driver))
        time.sleep(3)
        self.driver.find_element(*self.phone_confirm_button).click()
        time.sleep(3)

    def get_phone_number(self):
        return self.driver.find_element(*self.phone_number).text








