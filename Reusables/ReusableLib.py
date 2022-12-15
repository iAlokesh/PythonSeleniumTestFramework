import inspect
import logging

from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait


class ReusableLib:

    def __init__(self, driver):
        self.driver = driver

    def mouseactions(self):
        actions = ActionChains(self.driver)
        return actions

    def waitinstance(self, time):
        wait = WebDriverWait(self.driver, time)
        return wait

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler("logfile.log")
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)
        return logger
