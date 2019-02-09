from selenium import webdriver
import time
import unittest
import HtmlTestRunner
from SampleProject.POMDemo.Pages.loginPage import LoginPage
from SampleProject.POMDemo.Pages.homePage import HomePage


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("C:/Users/vivekkumarg/PycharmProjects/Practice/browser/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
        driver = self.driver

        driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")

        login = LoginPage(driver)
        login.enter_username('Admin')
        login.enter_password('admin123')
        login.click_login()

        time.sleep(4)

        home = HomePage(driver)
        home.click_welcome()
        home.click_logout()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        print("Test Completed")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner('C:/Users/vivekkumarg/PycharmProjects/Practice/reports'))
