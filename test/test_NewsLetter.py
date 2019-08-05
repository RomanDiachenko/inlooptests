# Open page, scroll in object, press in first newsletter, open page, go to first page
def test_openNewsletter(app):
    app.page_operation.open_page("https://athletictrainers.inloop.com")
    app.newsletter.scroll_to_newsletter()
    app.newsletter.click_in_first_newsletter()
    app.tab_operation.test_jump_to_page("https://athletictrainers.inloop.com/en/news")


# Open mail page and open all newsletter
def test_open_all_newsletter(app):
    app.newsletter.open_some_tab()
    app.newsletter.opennewsletter(2)
    app.newsletter.opennewsletter(3)
    app.newsletter.opennewsletter(4)
    app.newsletter.opennewsletter(5)
    app.newsletter.check_tab()
