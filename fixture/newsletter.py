import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


Newsletter_selector = "body.ng-scope.ng-isolate-scope:nth-child(2) div.mm-page.mm-slideout:nth-child(4) div.flex-wrapper.ng-scope:nth-child(1) template-page.ng-isolate-scope div.container.main-wrapper div.margin-top-1.main-content.mag-content.clearfix div.row.ng-scope:nth-child(2) div.col-md-4.ng-scope div.ng-scope div.ng-scope newsletters-archive.ng-isolate-scope:nth-child(13) div.widget.reviewwidget.newsletters div:nth-child(2) article.widget-post.clearfix.ng-scope:nth-child(%d) header:nth-child(2) h3.ng-scope > a.ng-binding"


class OperationWithNewsletter:

    def __init__(self, app):
        self.app = app

    # Click in first newsletter
    def click_in_first_newsletter(self):
        driver = self.app.driver
        driver.find_element_by_css_selector("newsletters-archive article header h3 a").click()
        time.sleep(2)

    # Scroll page to first newsletter
    def scroll_to_newsletter(self):
        driver = self.app.driver
        element = driver.find_element_by_css_selector(
            "newsletters-archive article header h3 a")
        ActionChains(driver).move_to_element(element).click().send_keys(Keys.PAGE_DOWN).perform()
        time.sleep(2)

    # Open some tab
    def open_some_tab(self):
        second_tab = self.app.driver.window_handles[0]
        print(second_tab)
        first_tab = self.app.driver.current_window_handle
        print(first_tab)

    # Open 2,3,4,5 newsletter
    def open_newsletter(self, child_element):
        driver = self.app.driver
        driver.find_element_by_css_selector(Newsletter_selector % child_element).click()
        first_tab = self.page_handle()
        self.app.driver.switch_to.window(first_tab)
        time.sleep(2)

    # Check opened window
    def page_handle(self):
        second_tab = self.app.driver.window_handles[0]
        print(second_tab)
        first_tab = self.app.driver.current_window_handle
        print(first_tab)
        return first_tab

    # Validation of the number of open tabs
    def check_opened_tab_count(self):
        all_page = self.app.driver.window_handles
        print(len(all_page))
        time.sleep(3)
        assert (len(all_page)) == 6
