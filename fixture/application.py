from selenium import webdriver
from fixture.newsletter import OperationWithNewsletter
from fixture.tab_operation import TabHelper
from fixture.page_operation import PageHelper


class Application:

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.newsletter = OperationWithNewsletter(self)
        self.tab_operation = TabHelper(self)
        self.page_operation = PageHelper(self)

    def open_page(self):
        driver = self.driver
        driver.get("https://athletictrainers.inloop.com")
        driver.find_element_by_tag_name('html')

    def destroy(self):
        self.driver.quit()
