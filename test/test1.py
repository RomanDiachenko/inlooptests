# Open page, scroll in object, press in first newsletter, open page, go to first page
def test_openNewsletter(app):
    app.newsletter.scroll_to_newsletter()
    app.newsletter.click_in_first_newsletter()
    app.tab_operation.test_jump_to_page()


def test_open_all_newsletter(app):
    app.newsletter.scroll_to_newsletter()
    app.newsletter.open_some_tab()
