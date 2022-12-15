import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from Reusables.TestDataReader import TestDataReader


class HomePage:

    # constructor
    def __init__(self, driver, reusableLib, log):
        self.driver = driver
        self.reusableLib = reusableLib
        self.log = log

    # locators
    __hotelsLink = (By.CSS_SELECTOR, "span.icon-hotels")
    __selectCity = (By.NAME, "BE_hotel_destination")
    __selectLocation = (By.XPATH, "//*[contains(text(),'Andheri East')]")
    __searchHotelsBtn = (By.CSS_SELECTOR, "#BE_hotel_htsearch_btn")

    # functions
    def clickHotelsLink(self):
        self.driver.find_element(*self.__hotelsLink).click()
        self.log.info("Hotels link has been clicked")
        self.log.info(TestDataReader.get_testdata("TC01")["url"])
        time.sleep(5)

    def type_city_name(self):
        actions = self.reusableLib.mouseactions()
        actions.move_to_element(self.driver.find_element(*self.__selectCity)).click().perform()
        time.sleep(5)
        wait = self.reusableLib.waitinstance(15)
        wait.until(expected_conditions.visibility_of_element_located(self.__selectCity)).send_keys("Mumbai")
        self.log.info("Mumbai has been passed as Place")
        time.sleep(5)
        assert self.driver.find_element(*self.__selectLocation).text == "Andheri East, Mumbai, India (174 hotels)"
        actions.move_to_element(self.driver.find_element(*self.__selectLocation)).click().perform()
        self.log.info("Andheri East has been selected as Location")
        time.sleep(10)

    def select_checkin_checkout_date(self):
        pass

    def click_search_hotels_btn(self):
        self.driver.find_element(*self.__searchHotelsBtn).click()
        time.sleep(10)
