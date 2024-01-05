import unittest
from time import sleep

from selenium import webdriver

from main import driver

driver.get('https://explore.hubtel.com/wp-content/themes/explorehubtel/images/stay-informed.png')

time.sleep(10)
class Login(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Firefox()
        self.driver.get("https://explore.hubtel.com/schools/")
        self.driver.maximize_window()
        sleep(4)

    def test_user_can_login(self):
        self.driver.find_element_by_xpath("//input[@id='loginPage:loginForm:username']").clear()
        self.driver.find_element_by_xpath("//input[@id='loginPage:loginForm:username']").send_keys("#####")
        self.driver.find_element_by_xpath("//input[@id='loginPage:loginForm:password']").send_keys("#####")
        self.driver.find_element_by_xpath("//input[@id='loginPage:loginForm:loginButton']").click()


    def tearDown(self) -> None:
        self.driver.close()


if __name__ == '__main__':
    unittest.main()