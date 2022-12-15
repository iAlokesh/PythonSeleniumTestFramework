import pytest


@pytest.fixture(scope="class")
def set_up():
    print("BeforeTest")
    yield
    print("AfterTest")


@pytest.fixture()
def dataset():
    return ["Alokesh", "Dey", "Python"]


@pytest.fixture(params=[("Hello","Hi"),"Whatsup"])
def paraset(request):
    return request.param

