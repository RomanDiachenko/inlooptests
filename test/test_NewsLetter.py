# Open page, scroll in object, press in first newsletter, open page, go to first page
def test_openNewsletter(app):
    app.page_operation.open_page("https://athletictrainers.inloop.com")
    app.newsletter.scroll_to_newsletter()
    app.newsletter.click_in_first_newsletter()
    app.tab_operation.test_jump_to_page("https://athletictrainers.inloop.com/en/news")


# Open mail page and open all newsletter
def test_open_all_newsletter(app):
    app.newsletter.open_some_tab()
    app.newsletter.open2newsletter()
    app.newsletter.open3newsletter()
    app.newsletter.open4newsletter()
    app.newsletter.open5newsletter()
    app.newsletter.check_tab()