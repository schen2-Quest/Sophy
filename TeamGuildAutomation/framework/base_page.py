from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    def clickOnElement(self, xpath):
        elm = self.waitForElementIsClickable(xpath)
        elm.click()

    def inputValue(self, xpath, text_value):
        elm = self.waitForElementIsVisible(xpath)
        elm.clear()
        elm.send_keys(text_value)

    def stringIsEqual(self, expected_result, actal_result, msg):
        try:
            self.assertEqual(expected_result, actal_result)
            print(msg)
        except AssertionError as e:
            raise e

    '''判断某个元素是否被添加到了dom里并且可见，可见代表元素可显示且宽和高都大于0'''
    def waitForElementIsVisible(self, xpath, waittime=60):
        try:
            elm = WebDriverWait(self.driver, waittime).until(
                EC.visibility_of_element_located((By.XPATH, xpath)))
        except Exception as e:
            print("Wait for element is time out.", xpath)

            raise e
        return elm

    '''判断title,返回布尔值'''
    def waitForTitleIsExpected(self, expected_title):
        try:
            WebDriverWait(self.driver, 60).until(EC.title_is(expected_title))
        except Exception as e:
            print("Title is not expected.")
            raise e

    '''判断某个元素中是否可见并且是enable的，代表可点击'''
    def waitForElementIsClickable(self, xpath, waittime=60):
        try:
            elm = WebDriverWait(self.driver, waittime).until(
                EC.element_to_be_clickable((By.XPATH, xpath)))
        except Exception as e:
            print("Wait for element is time out.")
            raise e
        return elm