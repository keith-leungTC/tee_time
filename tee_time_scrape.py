#!/usr/bin/env python
# coding: utf-8

from selenium import webdriver as wd
import chromedriver_binary
import time
import datetime

wd = wd.Chrome()
wd.implicitly_wait(10)

#VARIABLES

email = "xxxxx"
pw = "xxxxxx"
cc = "1234123412341234"
cvv = "123"
address = "xxxxx"
postal_code = "xxxxx"

first_tee = "//*[@id=\"app-container\"]/div/div[2]/div/div[2]/div[2]/div[2]/div[1]/div/button"
second_tee = "//*[@id=\"app-container\"]/div/div[2]/div/div[2]/div[2]/div[2]/div[2]/div/button"
third_tee = "//*[@id=\"app-container\"]/div/div[2]/div/div[2]/div[2]/div[2]/div[3]/div/button"

tee_url = "https://city-of-burnaby-golf.book.teeitup.com/?course=5fc6afcfd62a025a3123401a&date=2021-08-30&golfers=4"

two_some = "#app-container > div > div.jss3 > div > div > div > div > div:nth-child(3) > div > div:nth-child(1) > button"
three_some ="#app-container > div > div.jss3 > div > div > div > div > div:nth-child(3) > div > div:nth-child(2) > button"
four_some = "#app-container > div > div.jss3 > div > div > div > div > div:nth-child(3) > div > div:nth-child(3) > button"

#Open the webpage

wd.get(tee_url)

login_1 = wd.find_element_by_xpath('//*[@id="header"]/div/div[3]/div/ul/li/button').click()

username = wd.find_element_by_xpath('//*[@id="txtUsername"]').send_keys(email)
pw = wd.find_element_by_xpath('//*[@id="txtPassword"]').send_keys(pw)
login_2 = wd.find_element_by_xpath('//*[@id="login"]/div[2]/div[1]/div/div/form/div/div[3]/button/span[1]').click()


#Wait until [HH, MM, SS]

#while True:
 #   now = datetime.datetime.now()
  #  current_time = [now.hour, now.minute, now.second]
   # if current_time == [6, 0, 0]:
    #    wd.get(tee_url)
    #    break
    #else:
     #   time.sleep(0.5)
    
#PICK WHICH TEE TIME (first_tee second_tee third_tee)

while True:
    try:
        wd.find_element_by_xpath(second_tee).click()
        break
    except:
        time.sleep(0.5)

#PICK GROUP SIZE (two_some threes_some four_some)

while True:
    try:
        wd.find_element_by_css_selector(four_some).click()
        break
    except:
        time.sleep(0.5)

agree_tos_button = wd.find_element_by_xpath('//*[@id="cboAgreeTOC"]').click()

continue_to_book_button = wd.find_element_by_xpath('//*[@id="app-container"]/div/div[2]/div/div/div/div/div[8]/button').click()

while True:
    try:
        cc_number = wd.find_element_by_xpath('//*[@id="app-container"]/div/div[2]/form/div[2]/div[1]/div/div/div/div[1]/div/div/input').send_keys(cc)
        break
    except:
        time.sleep(0.5)

cc_exp_month_dropdown = wd.find_element_by_xpath('//*[@id="app-container"]/div/div[2]/form/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div').click()

cc_exp_month_select = wd.find_element_by_xpath('//*[@id="menu-Payment.CC.ExpirationMonth"]/div[2]/ul/li[6]').click()

cc_exp_year_dropdown = wd.find_element_by_xpath('//*[@id="app-container"]/div/div[2]/form/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div/div').click()

cc_exp_year_select = wd.find_element_by_xpath('//*[@id="menu-Payment.CC.ExpirationYear"]/div[2]/ul/li[6]').click()

time.sleep(.5)

cc_cvv = wd.find_element_by_xpath('//*[@id="app-container"]/div/div[2]/form/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div/input').send_keys(cvv)

cc_address = wd.find_element_by_xpath('//*[@id="app-container"]/div/div[2]/form/div[2]/div[1]/div/div/div/div[4]/div/input').send_keys(address)

cc_postal = wd.find_element_by_xpath('//*[@id="app-container"]/div/div[2]/form/div[2]/div[1]/div/div/div/div[5]/div[1]/div/input').send_keys(postal_code)

cc_country = wd.find_element_by_xpath('//*[@id="app-container"]/div/div[2]/form/div[2]/div[1]/div/div/div/div[5]/div[2]/div/div/div').click()

cc_country_select = wd.find_element_by_xpath('//*[@id="menu-Payment.Address.Country"]/div[2]/ul/li[3]').click()

make_reservation_button = wd.find_element_by_xpath('//*[@id="app-container"]/div/div[2]/form/div[2]/div[2]/div[8]/button').click()
