import time

from selenium import webdriver
from test.newsletter import OperationWithNewsletter
from tab_operation import TabHelper


class Application:

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="D:\Drivers\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.newsletter = OperationWithNewsletter(self)
        self.tab_operation = TabHelper(self)

    def open_page(self):
        driver = self.driver
        driver.get("https://athletictrainers.inloop.com")
        driver.find_element_by_tag_name('html')

    def test_open_some_tab(self):
        driver = self.driver
        second_tab = self.driver.window_handles
        print(second_tab)
        first_tab = self.driver.current_window_handle
        print(first_tab)
        driver.find_element_by_css_selector(
            "body.ng-scope.ng-isolate-scope:nth-child(3) div.mm-page.mm-slideout:nth-child(4) div.flex-wrapper.ng-scope:nth-child(1) template-page.ng-isolate-scope div.container.main-wrapper div.margin-top-1.main-content.mag-content.clearfix div.row.ng-scope:nth-child(2) div.col-md-4.ng-scope div.ng-scope div.ng-scope newsletters-archive.ng-isolate-scope:nth-child(13) div.widget.reviewwidget.newsletters div:nth-child(2) article.widget-post.clearfix.ng-scope:nth-child(2) header:nth-child(2) h3.ng-scope > a.ng-binding").click()
        time.sleep(2)
        self.driver.switch_to.window(first_tab)
        driver.find_element_by_css_selector(
            "body.ng-scope.ng-isolate-scope:nth-child(3) div.mm-page.mm-slideout:nth-child(4) div.flex-wrapper.ng-scope:nth-child(1) template-page.ng-isolate-scope div.container.main-wrapper div.margin-top-1.main-content.mag-content.clearfix div.row.ng-scope:nth-child(2) div.col-md-4.ng-scope div.ng-scope div.ng-scope newsletters-archive.ng-isolate-scope:nth-child(13) div.widget.reviewwidget.newsletters div:nth-child(2) article.widget-post.clearfix.ng-scope:nth-child(3) header:nth-child(2) h3.ng-scope > a.ng-binding").click()
        self.driver.switch_to.window(first_tab)
        driver.find_element_by_css_selector(
            "body.ng-scope.ng-isolate-scope:nth-child(3) div.mm-page.mm-slideout:nth-child(4) div.flex-wrapper.ng-scope:nth-child(1) template-page.ng-isolate-scope div.container.main-wrapper div.margin-top-1.main-content.mag-content.clearfix div.row.ng-scope:nth-child(2) div.col-md-4.ng-scope div.ng-scope div.ng-scope newsletters-archive.ng-isolate-scope:nth-child(13) div.widget.reviewwidget.newsletters div:nth-child(2) article.widget-post.clearfix.ng-scope:nth-child(4) header:nth-child(2) h3.ng-scope > a.ng-binding").click()
        self.driver.switch_to.window(first_tab)
        driver.find_element_by_css_selector(
            "body.ng-scope.ng-isolate-scope:nth-child(3) div.mm-page.mm-slideout:nth-child(4) div.flex-wrapper.ng-scope:nth-child(1) template-page.ng-isolate-scope div.container.main-wrapper div.margin-top-1.main-content.mag-content.clearfix div.row.ng-scope:nth-child(2) div.col-md-4.ng-scope div.ng-scope div.ng-scope newsletters-archive.ng-isolate-scope:nth-child(13) div.widget.reviewwidget.newsletters div:nth-child(2) article.widget-post.clearfix.ng-scope:nth-child(5) header:nth-child(2) h3.ng-scope > a.ng-binding").click()
        self.driver.switch_to.window(first_tab)

    def destroy(self):
        self.driver.quit()