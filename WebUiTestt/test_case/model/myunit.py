import unittest
from test_case.model.driver import browser


class MyTest(unittest.TestCase):
        def setUp(self):
            print("----Setup------------")
            self.driver = browser()
            self.driver.implicitly_wait(10)
            self.driver.maximize_window()

        def tearDown(self):
            print("----teardown----------")
            self.driver.quit()


if __name__ == '__main__':
        unittest.main()