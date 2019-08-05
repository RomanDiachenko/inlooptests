import time


class TabHelper:
    def __init__(self, app):
        self.app = app

    def test_jump_to_page(self):
        second_tab = self.app.driver.window_handles[0]
        print(second_tab)
        first_tab = self.app.driver.current_window_handle
        print(first_tab)
        time.sleep(2)
        self.app.driver.switch_to.window(second_tab)
        time.sleep(2)
        page_url = self.app.driver.current_url
        print(page_url)
        expected_url = "https://athletictrainers.inloop.com/en/news"
        assert expected_url == page_url


