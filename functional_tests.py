from selenium import webdriver
import os
import time

browser = webdriver.Firefox()
browser.get('http://localhost:8000')

assert 'Django' in browser.title

time.sleep(10)
browser.quit()
