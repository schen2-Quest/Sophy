from selenium.webdriver.common.by import By
from test_case.page_obj.base import Page
from time import sleep


class Login(Page):
    url = '/'
    #sign in
    login_username_loc = (By.ID, "cui-focusable")
    login_password_loc = (By.NAME, "cuiPassword")
    login_button_loc = (By.XPATH, "//button[@type='submit']")
    create_user_link_text_loc = (By.LINK_TEXT, "Users")
    #create user
    create_user_link_text_loc = (By.LINK_TEXT, "Users")
    create_user_button_loc = (By.XPATH, "(//button[@type='button'])[3]")
    create_user_contAddTICUser_loc = (By.ID, "contAddTICUser")
    create_user_popICUserUserName_loc = (By.ID, "popICUserUserName")
    create_user_popICUserFullName_loc = (By.ID, "popICUserFullName")
    create_user_popICUserEmail_loc = (By.ID, "popICUserEmail")
    create_user_popICUserPassword_loc = (By.ID, "popICUserPassword")
    create_user_popICUserConfPassword_loc = (By.ID, "popICUserConfPassword")
    create_user_popICUserCreate_loc = (By.ID, "popICUserCreate")
    register_user_success_loc = (By.CLASS_NAME, "ng-binding")

    def login_username(self, username):
        self.send_keys(self.login_username_loc, username, True, False)

    def login_password(self, password):
        self.find_element(*self.login_password_loc).clear()
        self.find_element(*self.login_password_loc).send_keys(password)

    def login_button(self):
        self.find_element(*self.login_button_loc).click()

    def user_login(self, username="root", password="123"):
        self.open()
        self.login_username(username)
        self.login_password(password)
        sleep(3)
        self.login_button()
        sleep(5)

    def register_user(self, username="test_user", fullname="tests", email="test_user@gmail.com", password="123",
                      confirm_password="123"):
        self.find_element(*self.create_user_link_text_loc).click()
        self.find_element(*self.create_user_button_loc).click()
        self.find_element(*self.create_user_contAddTICUser_loc).click()
        self.find_element(*self.create_user_popICUserUserName_loc).send_keys(username)
        self.find_element(*self.create_user_popICUserFullName_loc).send_keys(fullname)
        self.find_element(*self.create_user_popICUserEmail_loc).send_keys(email)
        self.find_element(*self.create_user_popICUserPassword_loc).send_keys(password)
        self.find_element(*self.create_user_popICUserConfPassword_loc).send_keys(confirm_password)
        self.find_element(*self.create_user_popICUserCreate_loc).click()
        sleep(5)
        account_information = self.driver.find_elements_by_class_name("ng-binding")
        flag = False
        for item in account_information:
            context = item.text
            print("context : ", context)
            if (context == "test_user (tests)"):
                flag = True
                break
        assert flag, "the new user not found %s" % username
