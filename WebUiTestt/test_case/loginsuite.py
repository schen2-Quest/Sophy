import unittest
import test_case.login_sta


def suite1():
    suite = unittest.TestSuite()
    suite.addTest(test_case.login_sta.LoginTest('test_sign_exist_account'))
    print("---suite1--")
    return suite


def suite2():
    # print("---suite2--")
    suite = unittest.TestSuite()
    suite.addTest(test_case.login_sta.LoginTest('test_register_new_user'))
    return suite


def all_suite():
    print("---suite---all-")
    suite = unittest.TestSuite((suite1(), suite2()))
    return suite


