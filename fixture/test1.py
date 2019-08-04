import pytest

from test.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_my_tests(app):
    app.open_page()
    app.newsletter.scroll_to_newsletter()
    app.newsletter.click_in_first_newsletter()
    app.tab_operation.test_jump_to_page("/en/api/feedlandingapi/getnewslettertemplatebody?id=6708")
    # self.open_some_tab()

