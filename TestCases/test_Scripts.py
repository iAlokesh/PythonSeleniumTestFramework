import pytest
from Reusables.BaseTest import BaseTest


class TestScripts(BaseTest):

    def test_Scripts(self):

        self.init_page_objects()
        self.hp.clickHotelsLink()
        self.hp.type_city_name()
        self.hp.click_search_hotels_btn()


