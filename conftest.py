import pytest

from fixture.application import Application


# scope = session it's a command where browser run all tests in one window
@pytest.fixture(scope="session")
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture
