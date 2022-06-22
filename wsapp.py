from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

phone_number = "#contact"
photo_path = '/path-to-image.jpg'

#open whatsapp web from selenium
service = Service(executable_path='/path-to-chrome-driver')
driver = webdriver.Chrome(service = service)
driver.get('https://web.whatsapp.com/')
driver.maximize_window()
time.sleep(30)

#inspect and select search element
search_phone = driver.find_element(by='xpath', value='//div[@title="Search input textbox"]')
search_phone.send_keys(phone_number)  # write contact number here
time.sleep(5)

#to search contact from search box and open it's chat
contacts = driver.find_elements(by='xpath', value='//div[@aria-label="Search results."]//div[@data-testid="cell-frame-container"]')
contacts[-1].click()  # picks last element in the list (this one represents first in the whatsapp search list)
time.sleep(5)

# to attach image from attachments
attach_button = driver.find_element(by='xpath', value='//span[@data-testid="clip"]')
attach_button.click()
time.sleep(5)

#During inspect, chose element which has the word "input"
attach_image_input = driver.find_element(by='xpath', value='//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
attach_image_input.send_keys(photo_path)
time.sleep(5)

#For sending the image 
send_image_button = driver.find_element(by='xpath', value='//div[@data-testid="drawer-middle"]//span[@data-testid="send"]')
send_image_button.click()
time.sleep(10)  # wait till the message is delivered

driver.quit()