from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import requests
import lxml.html
import sys
import codecs

time.sleep(2)
browser = webdriver.Chrome()
#browser.get("https://www.evernote.com/Login.action")
browser.get("https://www.tijd.be/mijn-diensten/registratie/wijzigen?fromlink=true&forceLogin=true")
time.sleep(5)
#username = browser.find_element_by_id("username")
username = browser.find_element_by_id("email")
username.send_keys("peter.mostmans@telenet.be")
login_attempt = browser.find_element_by_xpath("//*[@type='submit']")
login_attempt.submit()
time.sleep(5)
password = browser.find_element_by_id("password")
password.send_keys("nicetry1")
login_attempt = browser.find_element_by_xpath("//*[@type='submit']")
login_attempt.submit()
time.sleep(3)
#simuleer het aanklikken van de link met naam 'portefeuille'
elem = browser.find_element_by_link_text("Portefeuille")
elem.click()

#browser.quit()
