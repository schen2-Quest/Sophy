from time import sleep
from test_case.model import myunit
from test_case.model import function
from test_case.page_obj.loginPage import Login
import time


class LoginTest(myunit.MyTest):

    def log_info(self, text):
        print("<font color>='#696969'\t- %s: %s</font>" % (time.strftime('%X', time.localtime(time.time())), text))

    def user_login_verify(self, username="", password=""):
        print("..........................")
        Login(self.driver).user_login(username, password)

    def test_sign_exist_account(self):
        """test_sign_exist_account"""
        self.log_info("sign inssssssssssssssss")
        self.user_login_verify(username="root",password="123")

    def test_register_new_user(self):
        """test_register_new_user"""
        self.log_info("sign inmmmmmmmm")
        self.user_login_verify(username="root",password="123")
        sleep(3)
        po = Login(self.driver)
        function.insert_img(self.driver, "user_pwd_true.png")
        po.register_user(username="test_user", fullname="tests", email="test_user@gmail.com", password="123", confirm_password="123")
