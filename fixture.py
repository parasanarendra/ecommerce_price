import pytest

@pytest.fixture()
def setup():
    print("I will excuting first")
def fixturedemo(setup):
    print("I will executes steps in fixtures demo")

