from selenium import webdriver
import time

browser = webdriver.Firefox()
browser.get("https://ru.wikipedia.org/wiki/История_штата_Нью-Йорк")
time.sleep(10)
browser.quit()
