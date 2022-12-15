import time

from selenium.webdriver.common.by import By


class HotelSearchResultPage:

    # class variables
    driver = None
    wait = None

    # constructor
    def __init__(self, d):
        HotelSearchResultPage.driver = d

    # locators
    __listOfHotelsEle = (By.XPATH, "//div[@view-mode='list']/article/div")

    # methods
    def select_second_hotel_in_the_search_page(self):
        listOfHotels = self.driver.find_elements(*self.__listOfHotelsEle)
        print(len(listOfHotels))
        time.sleep(5)
        print(listOfHotels[1])
