from time import sleep
import unittest
from test_case.model import myunit
from test_case.model import function
from test_case.page_obj.loginPage import Login


class LoginTest(myunit.MyTest):

    def user_login_verify(self, username="", password=""):
        Login(self.driver).user_login(username, password)

    def test_login5(self):
        self.user_login_verify(username="root",password="123")
        sleep(3)
        po = Login(self.driver)
        function.insert_img(self.driver, "user_pwd_true.png")
        po.register_user(username="test_user", fullname="tests", email="test_user@gmail.com", password="123", confirm_password="123")


if __name__ == '__main__':
    unittest.main()