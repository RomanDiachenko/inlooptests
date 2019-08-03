import pytest

from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_my_tests(app):
    app.open_page()
    app.scroll_to_newsletter()
    app.click_in_first_newsletter()
    app.test_jump_to_page("/en/api/feedlandingapi/getnewslettertemplatebody?id=6708")
    # self.open_some_tab()

