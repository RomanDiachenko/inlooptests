# Open page, scroll in object, press in first newsletter, open page, go to first page
def test_openNewsletter(app):
    app.page_operation.open_page("https://athletictrainers.inloop.com")
    app.newsletter.scroll_to_newsletter()
    app.newsletter.click_in_first_newsletter()
    app.tab_operation.test_jump_to_page("https://athletictrainers.inloop.com/en/news")


# Open mail page and open all newsletter
def test_open_all_newsletter(app):
    app.newsletter.open_some_tab()
    app.newsletter.open_newsletter(2)
    app.newsletter.open_newsletter(3)
    app.newsletter.open_newsletter(4)
    app.newsletter.open_newsletter(5)
    app.newsletter.check_opened_tab_count()
