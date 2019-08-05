import time


class PageHelper:

    def __init__(self, app):
        self.app = app

    def open_page(self):
        driver = self.app.driver
        driver.get("https://athletictrainers.inloop.com")
        driver.find_element_by_tag_name('html')
        time.sleep(5)
