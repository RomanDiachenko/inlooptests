import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class newsletter_jump:
    def __init__(self, app):
        self.app = app

    def click_in_first_newsletter(self):
        driver = self.app.driver
        driver.find_element_by_css_selector(
            "body.ng-scope.ng-isolate-scope:nth-child(2) div.mm-page.mm-slideout:nth-child(4) div.flex-wrapper.ng-scope:nth-child(1) template-page.ng-isolate-scope div.container.main-wrapper div.margin-top-1.main-content.mag-content.clearfix div.row.ng-scope:nth-child(2) div.col-md-4.ng-scope div.ng-scope div.ng-scope newsletters-archive.ng-isolate-scope:nth-child(13) div.widget.reviewwidget.newsletters div:nth-child(2) article.widget-post.clearfix.ng-scope:nth-child(1) header:nth-child(2) h3.ng-scope > a.ng-binding").click()
        time.sleep(10)

    def scroll_to_newsletter(self):
        self.app.open_page()
        driver = self.app.driver
        element = driver.find_element_by_css_selector(
            "body.ng-scope.ng-isolate-scope:nth-child(2) div.mm-page.mm-slideout:nth-child(4) div.flex-wrapper.ng-scope:nth-child(1) template-page.ng-isolate-scope div.container.main-wrapper div.margin-top-1.main-content.mag-content.clearfix div.row.ng-scope:nth-child(2) div.col-md-4.ng-scope div.ng-scope div.ng-scope newsletters-archive.ng-isolate-scope:nth-child(13) div.widget.reviewwidget.newsletters div:nth-child(2) article.widget-post.clearfix.ng-scope:nth-child(1) header:nth-child(2) h3.ng-scope > a.ng-binding")
        ActionChains(driver).move_to_element(element).click().send_keys(Keys.PAGE_DOWN).perform()
        time.sleep(2)
