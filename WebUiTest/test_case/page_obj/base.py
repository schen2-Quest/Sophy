from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Page(object):

    base_url = "http://10.154.10.38"

    def __init__(self, selenium_driver, base_url=base_url, parent=None):
        self.base_url = base_url
        self.driver = selenium_driver
        self.timeout = 30
        self.parent = parent

    def _open(self, url):
        url = self.base_url + url
        self.driver.get(url)
        assert self.on_page(), 'Did not land on %s' % url

    def open(self):
        self._open(self.url)

    def on_page(self):
        return self.driver.current_url == (self.base_url + self.url)

    def find_element(self, *loc):
        try:
            print("loc",loc)
            print("*loc",*loc)
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except ():
            print(u"%s 页面中未能找到 %s 元素" % (self, loc))

    def script(self, src):
        return self.driver.execute_script(src)

    def switch_frame(self, loc):
        return self.driver.swith_to_frame(loc)

    def send_keys(self, loc, value, clear_first=True, click_first=True):
        try:
            print("*loc----",*loc)
            print("loc----",loc)
            if click_first:
                self.find_element(*loc).click()
            if clear_first:
                self.find_element(*loc).clear()
            self.find_element(*loc).send_keys(value)
        except ArithmeticError:
            print(u"%s 页面中未能找到 %s 元素" % (self, loc))