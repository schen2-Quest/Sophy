from framework.base_page import BasePage


class LoginPage(BasePage):

    username_box = "//input[@id='username']"
    password_box = "//input[@id='password']"
    submit_btn = "//button[@id='kc-login']"
    prompt_box = "//a[@class='_hj-f5b2a1eb-9b07_transition']"

    def input_username(self, text):
        self.inputValue(self.username_box, text)

    def input_password(self, text):
        self.inputValue(self.password_box, text)

    def send_submit_btn(self):
        self.clickOnElement(self.submit_btn)

    def assert_title(self,text):
        self.waitForTitleIsExpected(text)

    def process_message(self):
        self.element_is_exits(self.prompt_box, waittime=20, is_need_quit=False)