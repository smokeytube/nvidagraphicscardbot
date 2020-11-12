#Coded completely by smokeytube
import time as t
from sys import stdout
from selenium import webdriver
from optparse import OptionParser
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import os, sys
from discord_webhook import DiscordWebhook
import pyautogui


CHROME_DVR_DIR = 'C:\webdrivers\chromedriver.exe'
driver = webdriver.Chrome(CHROME_DVR_DIR)
driver.implicitly_wait(5)


#driver.get('https://www.newegg.com/evga-geforce-rtx-3080-10g-p5-3897-kr/p/N82E16814487518?Description=rtx%203080&cm_re=rtx_3080-_-14-487-518-_-Product&quicklink=true')
driver.get('https://www.newegg.com/royal-blue-asus-zenbook-15-ux534ftc-nh77-gaming-entertainment/p/N82E16834235471?Item=N82E16834235471&cm_sp=Homepage_MKPL-_-P1_34-235-471-_-11112020')


time.sleep(2)

while True:
    try:
        checkout = driver.find_element_by_xpath('//*[@id="ProductBuy"]/div/div[2]/button')
        checkout.click()
        if driver.find_element_by_xpath('//*[@id="modal-intermediary"]/div/div/div/div[3]/button[1]') == True:
            nothanks = driver.find_element_by_xpath('//*[@id="modal-intermediary"]/div/div/div/div[3]/button[1]')
            nothanks.click()

            viewcartncheckout = driver.find_element_by_xpath('//*[@id="modal-intermediary"]/div/div/div[2]/div[2]/button[2]')
            viewcartncheckout.click()

            securecheckout = driver.find_element_by_xpath('//*[@id="app"]/div[1]/section/div/div/form/div[2]/div[3]/div/div/div[3]/div/button')
            securecheckout.click()

            addlocation = driver.find_element_by_xpath('//*[@id="app"]/div/section/div/div/form/div[2]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/div/div')
            addlocation.click()
    except:
        #driver.refresh()
        pyautogui.press('f5')



