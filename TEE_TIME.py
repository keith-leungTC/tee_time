#!/usr/bin/env python
# coding: utf-8

from selenium import webdriver as wd
import time, datetime
from webdriver_manager.chrome import ChromeDriverManager

print('Please put in date in this format YYYY-MM-DD:')
play_date = input()

print('Put in the start time in 24 hour format (include leading zeroes) ie. 09:')
start_time = input()

print('Put in the end time in 24 hour format (include leading zeroes) ie. 09:')
end_time = input()

print('Which tee time? 1, 2, 3')
tee_time = input()

if tee_time == '1':
    tee_time = "//*[@id=\"app-container\"]/div/div[2]/div/div[2]/div[2]/div[2]/div[1]/div/button"
if tee_time == '2':
    tee_time = "//*[@id=\"app-container\"]/div/div[2]/div/div[2]/div[2]/div[2]/div[2]/div/button"
if tee_time == '3':
    tee_time = "//*[@id=\"app-container\"]/div/div[2]/div/div[2]/div[2]/div[2]/div[3]/div/button"

print('Which course? 1 for Burnaby. 2 for Riverway: ')
course_select = input()

if course_select == '1':
    course_select = "5fc6aee4135f8f0cadf85c79&"

if course_select == '2':
    course_select = "5fc6afcfd62a025a3123401a&"

print('How many players would you like to book for?')
players = input()

if players == '2':
    players = "#app-container > div > div.jss3 > div > div > div > div > div:nth-child(3) > div > div:nth-child(1) > button"
if players == '3':
    players = "#app-container > div > div.jss3 > div > div > div > div > div:nth-child(3) > div > div:nth-child(2) > button"
if players == '4':
    players = "#app-container > div > div.jss3 > div > div > div > div > div:nth-child(3) > div > div:nth-child(3) > button"

print('Please put in your email:')
email = input()

print('Please put in your password:')
pw = input()

print('Please put in your CC number:')
cc = input()

print('Please put in your cvv:')
cvv = input()

print('Please put in your address: ')
address = input()

print('Please put in your postal code: ')
postal_code = input()

wd = wd.Chrome(ChromeDriverManager().install())
wd.implicitly_wait(10)

# TESTING VARIABLES

#email = "XXXXXXXXXXXXXX"
#pw = "XXXXXXXX"
#cc = "XXXXXXXXXXXXXXXXX"
#cvv = "XXX"
#address = "XXXXXXXXXXXXXXXX"
#postal_code = "XXX XXX"

#first_tee = "//*[@id=\"app-container\"]/div/div[2]/div/div[2]/div[2]/div[2]/div[1]/div/button"
#second_tee = "//*[@id=\"app-container\"]/div/div[2]/div/div[2]/div[2]/div[2]/div[2]/div/button"
#third_tee = "//*[@id=\"app-container\"]/div/div[2]/div/div[2]/div[2]/div[2]/div[3]/div/button"

tee_url = "https://city-of-burnaby-golf.book.teeitup.com/?course={}&date={}&end={}&start={}".format(course_select, play_date, end_time, start_time)

#two_some = "#app-body > div.jss16.jss18.jss19 > div.jss1750.jss1776.jss1751.jss21.jss22.jss1737.jss25.jss27 > div.jss1778 > div:nth-child(2) > div:nth-child(1) > div > div > div > div:nth-child(1) > button"
#three_some ="#app-body > div.jss16.jss18.jss19 > div.jss1750.jss1776.jss1751.jss21.jss22.jss1737.jss25.jss27 > div.jss1778 > div:nth-child(2) > div:nth-child(1) > div > div > div > div:nth-child(2) > button"
#four_some = "#app-body > div.jss16.jss18.jss19 > div.jss1750.jss1776.jss1751.jss21.jss22.jss1737.jss25.jss27 > div.jss1778 > div:nth-child(2) > div:nth-child(1) > div > div > div > div:nth-child(3) > button"

#Open the webpage

wd.get(tee_url)

login_1 = wd.find_element_by_xpath('//*[@id="header"]/div/div[3]/div/ul/li/button').click()

username = wd.find_element_by_xpath('//*[@id="txtUsername"]').send_keys(email)
pw = wd.find_element_by_xpath('//*[@id="txtPassword"]').send_keys(pw)
login_2 = wd.find_element_by_xpath('//*[@id="login"]/div[2]/div[1]/div/div/form/div/div[3]/button/span[1]').click()

#Wait until [HH, MM, SS]

while True:
    now = datetime.datetime.now()
    current_time = [now.hour, now.minute, now.second]
    if current_time == [6, 0, 0]:
        break
    else:
        time.sleep(0.5)
    
#PICK WHICH TEE TIME (first_tee second_tee third_tee)

while True:
    try:
        wd.find_element_by_xpath(tee_time).click()
        break
    except:
        wd.get(tee_url)

#PICK GROUP SIZE (two_some threes_some four_some)

while True:
    try:
        wd.find_element_by_css_selector(players).click()
        break
    except:
        time.sleep(0.5)

continue_to_book_button = wd.find_element_by_xpath('//*[@id="app-body"]/div[2]/div[2]/div[3]/div/button[1]').click()

while True:
    try:
        cc_number = wd.find_element_by_xpath('//*[@id="app-container"]/div/div[2]/div[2]/div/div/div/div[1]/div/div[1]/div/div[1]/div/div/input').send_keys(cc)
        break                                   
    except:
        time.sleep(0.5)

cc_exp_month_dropdown = wd.find_element_by_xpath('//*[@id="app-container"]/div/div[2]/div[2]/div/div/div/div[1]/div/div[1]/div/div[2]/div[1]/div/div/div/div').click()
time.sleep(0.5)                                   
cc_exp_month_select = wd.find_element_by_xpath('//*[@id="menu-Payment.CC.ExpirationMonth"]/div[2]/ul/li[6]').click()

cc_exp_year_dropdown = wd.find_element_by_xpath('//*[@id="app-container"]/div/div[2]/div[2]/div/div/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div/div/div').click()
time.sleep(0.5)
cc_exp_year_select = wd.find_element_by_xpath('//*[@id="menu-Payment.CC.ExpirationYear"]/div[2]/ul/li[6]').click()

time.sleep(.5)

cc_cvv = wd.find_element_by_xpath('//*[@id="app-container"]/div/div[2]/div[2]/div/div/div/div[1]/div/div[1]/div/div[2]/div[3]/div/div/div/input').send_keys(cvv)

cc_address = wd.find_element_by_xpath('//*[@id="app-container"]/div/div[2]/div[2]/div/div/div/div[1]/div/div[1]/div/div[4]/div/input').send_keys(address)

cc_postal = wd.find_element_by_xpath('//*[@id="app-container"]/div/div[2]/div[2]/div/div/div/div[1]/div/div[1]/div/div[5]/div[1]/div/input').send_keys(postal_code)

cc_country = wd.find_element_by_xpath('//*[@id="app-container"]/div/div[2]/div[2]/div/div/div/div[1]/div/div[1]/div/div[5]/div[2]/div/div/div').click()

cc_country_select = wd.find_element_by_xpath('//*[@id="menu-Payment.Address.Country"]/div[2]/ul/li[3]').click()

agree_toc = wd.find_element_by_xpath('//*[@id="app-container"]/div/div[2]/div[2]/div/div/div/div[2]/div[9]/label/span[1]/span[1]/input').click()

make_reservation_button = wd.find_element_by_xpath('//*[@id="app-container"]/div/div[2]/div[2]/div/div/div/div[2]/div[11]/button').click()
