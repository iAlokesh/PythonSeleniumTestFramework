import pytest


@pytest.mark.usefixtures("set_up","dataset","paraset")
class TestPractice:

    @pytest.mark.smoke
    def test_add(self,paraset):
        i, j = 5, 10
        k = i + j
        print("{} {}".format(k,paraset[1]))
        #print(dataset)
