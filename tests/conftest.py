import pytest


@pytest.fixture()
def setup_teardown():
    print()
    print("***********I will be executed in the beginning***********")
    yield
    print("***********I will be executed in the end***********")