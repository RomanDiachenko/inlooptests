import time
import unittest

from selenium import webdriver

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class OpenBrowser(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="D:\Drivers\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_firsttap(self):
        driver = self.driver
        driver.get("https://athletictrainers.inloop.com")
        new_page = driver.find_element_by_tag_name('html')
        self.scroll_to_newsletter(driver)
        self.click_in_first_newsletter(driver)
        self.jump_to_paje()

    def jump_to_paje(self):
        s = self.driver.window_handles
        print(s)
        b = self.driver.current_window_handle
        print(b)
        time.sleep(2)
        self.driver.switch_to.window(b)
        time.sleep(2)

    def click_in_first_newsletter(self, driver):
        driver.find_element_by_css_selector(
            "body.ng-scope.ng-isolate-scope:nth-child(2) div.mm-page.mm-slideout:nth-child(4) div.flex-wrapper.ng-scope:nth-child(1) template-page.ng-isolate-scope div.container.main-wrapper div.margin-top-1.main-content.mag-content.clearfix div.row.ng-scope:nth-child(2) div.col-md-4.ng-scope div.ng-scope div.ng-scope newsletters-archive.ng-isolate-scope:nth-child(13) div.widget.reviewwidget.newsletters div:nth-child(2) article.widget-post.clearfix.ng-scope:nth-child(1) header:nth-child(2) h3.ng-scope > a.ng-binding").click()
        time.sleep(2)
        a = self.driver.current_url
        print(a)
        current_url = "https://athletictrainers.inloop.com/en/api/feedlandingapi/getnewslettertemplatebody?id=6708"
        assert current_url == "https://athletictrainers.inloop.com/en/api/feedlandingapi/getnewslettertemplatebody?id=6708"

    def scroll_to_newsletter(self, driver):
        element = driver.find_element_by_css_selector(
            '''body.ng-scope.ng-isolate-scope:nth-child(2) div.mm-page.mm-slideout:nth-child(4) div.flex-wrapper.ng-scope:nth-child(1) template-page.ng-isolate-scope div.container.main-wrapper div.margin-top-1.main-content.mag-content.clearfix div.row.ng-scope:nth-child(2) div.col-md-4.ng-scope div.ng-scope div.ng-scope newsletters-archive.ng-isolate-scope:nth-child(13) div.widget.reviewwidget.newsletters div:nth-child(2) article.widget-post.clearfix.ng-scope:nth-child(1) header:nth-child(2) h3.ng-scope > a.ng-binding''')
        ActionChains(driver).move_to_element(element).click().send_keys(Keys.PAGE_DOWN).perform()
        time.sleep(2)

    def tear_down(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
