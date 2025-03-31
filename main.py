import data
import helpers
from selenium import webdriver
from pages import UrbanRoutesPage
class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        # do not modify - we need additional logging enabled in order to retrieve phone confirmation code
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(5)
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Successfully connected to Urban Routes.")
        else:
            print("Cannot connect to Urban Routes. Check the server is on and still running")
    def test_set_route(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)
        page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        assert page.get_from() == data.ADDRESS_FROM
        assert page.get_to() == data.ADDRESS_TO
    def test_select_plan(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)
        page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        page.select_supportive_plan()
        assert page.get_current_selected_plan() == 'Supportive'
    def test_fill_phone_number(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)
        page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        page.select_supportive_plan()
        page.use_phone_number()
        assert page.get_phone_number() == data.PHONE_NUMBER
    def test_fill_card(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)
        page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        page.add_new_card(data.CARD_NUMBER, data.CARD_CODE)
        assert page.get_current_payment_method() == 'Card'
    def test_comment_for_driver(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)
        page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        page.enter_comment(data.MESSAGE_FOR_DRIVER)
        assert page.get_comment() == data.MESSAGE_FOR_DRIVER
    def test_order_blanket_and_handkerchiefs(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)
        page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        page.select_supportive_plan()
        page.select_blankets()
        assert page.get_blankets_and_handkerchiefs() == 'true'
    def test_order_2_ice_creams(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)
        page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        page.select_supportive_plan()
        for i in range(2):
           page.add_ice_cream()
        assert page.get_plus_ice_cream() == '2'
    def test_car_search_model_appears(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)
        page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        page.select_supportive_plan()
        page.enter_comment(data.MESSAGE_FOR_DRIVER)
        page.order_taxi()
        assert page.car_search_displayed()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()