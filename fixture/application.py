from selenium import webdriver
from fixture.newsletter import OperationWithNewsletter
from fixture.tab_operation import TabHelper
from fixture.page_operation import PageHelper


class Application:

    def __init__(self, chromedriver):
        self.driver = webdriver.Chrome(executable_path=chromedriver)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.newsletter = OperationWithNewsletter(self)
        self.tab_operation = TabHelper(self)
        self.page_operation = PageHelper(self)

    def open_page(self, url):
        driver = self.driver
        driver.get(url)
        driver.find_element_by_tag_name('html')

    def destroy(self):
        self.driver.quit()
