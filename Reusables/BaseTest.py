import pytest
from PageObjects.HomePage import HomePage
from Reusables.ReusableLib import ReusableLib


@pytest.mark.usefixtures("setup")
class BaseTest:
    hp = None
    log = None

    def init_page_objects(self):
        reusableLib = ReusableLib(self.driver)
        BaseTest.log = reusableLib.getLogger()
        BaseTest.hp = HomePage(self.driver, reusableLib, self.log)
