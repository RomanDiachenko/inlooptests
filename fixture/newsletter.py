import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class OperationWithNewsletter:

    def __init__(self, app):
        self.app = app

    # Click in first newsletter
    def click_in_first_newsletter(self):
        driver = self.app.driver
        driver.find_element_by_css_selector(
            "body.ng-scope.ng-isolate-scope:nth-child(2) div.mm-page.mm-slideout:nth-child(4) div.flex-wrapper.ng-scope:nth-child(1) template-page.ng-isolate-scope div.container.main-wrapper div.margin-top-1.main-content.mag-content.clearfix div.row.ng-scope:nth-child(2) div.col-md-4.ng-scope div.ng-scope div.ng-scope newsletters-archive.ng-isolate-scope:nth-child(13) div.widget.reviewwidget.newsletters div:nth-child(2) article.widget-post.clearfix.ng-scope:nth-child(1) header:nth-child(2) h3.ng-scope > a.ng-binding").click()
        time.sleep(10)

    # Scroll page to first newsletter
    def scroll_to_newsletter(self):
        self.app.open_page()
        driver = self.app.driver
        element = driver.find_element_by_css_selector(
            "body.ng-scope.ng-isolate-scope:nth-child(2) div.mm-page.mm-slideout:nth-child(4) div.flex-wrapper.ng-scope:nth-child(1) template-page.ng-isolate-scope div.container.main-wrapper div.margin-top-1.main-content.mag-content.clearfix div.row.ng-scope:nth-child(2) div.col-md-4.ng-scope div.ng-scope div.ng-scope newsletters-archive.ng-isolate-scope:nth-child(13) div.widget.reviewwidget.newsletters div:nth-child(2) article.widget-post.clearfix.ng-scope:nth-child(1) header:nth-child(2) h3.ng-scope > a.ng-binding")
        ActionChains(driver).move_to_element(element).click().send_keys(Keys.PAGE_DOWN).perform()
        time.sleep(2)

    # Open some tab
    def open_some_tab(self):
        driver = self.app.driver
        second_tab = self.app.driver.window_handles
        print(second_tab)
        first_tab = self.app.driver.current_window_handle
        print(first_tab)
        driver.find_element_by_css_selector(
            "body.ng-scope.ng-isolate-scope:nth-child(8) div.mm-page.mm-slideout:nth-child(4) div.flex-wrapper.ng-scope:nth-child(1) template-page.ng-isolate-scope div.container.main-wrapper div.margin-top-1.main-content.mag-content.clearfix div.row.ng-scope:nth-child(2) div.col-md-4.ng-scope div.ng-scope div.ng-scope newsletters-archive.ng-isolate-scope:nth-child(13) div.widget.reviewwidget.newsletters div:nth-child(2) article.widget-post.clearfix.ng-scope:nth-child(2) header:nth-child(2) h3.ng-scope > a.ng-binding").click()
        time.sleep(2)
        self.app.driver.switch_to.window(first_tab)
        driver.find_element_by_css_selector(
            "body.ng-scope.ng-isolate-scope:nth-child(3) div.mm-page.mm-slideout:nth-child(4) div.flex-wrapper.ng-scope:nth-child(1) template-page.ng-isolate-scope div.container.main-wrapper div.margin-top-1.main-content.mag-content.clearfix div.row.ng-scope:nth-child(2) div.col-md-4.ng-scope div.ng-scope div.ng-scope newsletters-archive.ng-isolate-scope:nth-child(13) div.widget.reviewwidget.newsletters div:nth-child(2) article.widget-post.clearfix.ng-scope:nth-child(3) header:nth-child(2) h3.ng-scope > a.ng-binding").click()
        self.app.driver.switch_to.window(first_tab)
        driver.find_element_by_css_selector(
            "body.ng-scope.ng-isolate-scope:nth-child(3) div.mm-page.mm-slideout:nth-child(4) div.flex-wrapper.ng-scope:nth-child(1) template-page.ng-isolate-scope div.container.main-wrapper div.margin-top-1.main-content.mag-content.clearfix div.row.ng-scope:nth-child(2) div.col-md-4.ng-scope div.ng-scope div.ng-scope newsletters-archive.ng-isolate-scope:nth-child(13) div.widget.reviewwidget.newsletters div:nth-child(2) article.widget-post.clearfix.ng-scope:nth-child(4) header:nth-child(2) h3.ng-scope > a.ng-binding").click()
        self.app.driver.switch_to.window(first_tab)
        driver.find_element_by_css_selector(
            "body.ng-scope.ng-isolate-scope:nth-child(3) div.mm-page.mm-slideout:nth-child(4) div.flex-wrapper.ng-scope:nth-child(1) template-page.ng-isolate-scope div.container.main-wrapper div.margin-top-1.main-content.mag-content.clearfix div.row.ng-scope:nth-child(2) div.col-md-4.ng-scope div.ng-scope div.ng-scope newsletters-archive.ng-isolate-scope:nth-child(13) div.widget.reviewwidget.newsletters div:nth-child(2) article.widget-post.clearfix.ng-scope:nth-child(5) header:nth-child(2) h3.ng-scope > a.ng-binding").click()
        self.app.driver.switch_to.window(first_tab)
