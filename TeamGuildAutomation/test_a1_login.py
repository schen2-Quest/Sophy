import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.login_page import LoginPage
import time

class ScanPage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):

        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser()

    @classmethod
    def tearDownClass(cls):

        cls.driver.quit()

    def test_a1__login(self):
        loginpage = LoginPage(self.driver)
        loginpage.input_username("dev100@snapmail.cc")
        loginpage.input_password("Quest123")
        loginpage.send_submit_btn()
        loginpage.assert_title("Onboarding")

if __name__ == '__main__':
    unittest.main()