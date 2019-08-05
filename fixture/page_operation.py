import time


class PageHelper:

    def __init__(self, app):
        self.app = app

    def open_page(self, url):
        driver = self.app.driver
        driver.get(url)
        driver.find_element_by_tag_name('html')
        time.sleep(5)
