from selenium import webdriver
import time

option = webdriver.ChromeOptions()
option.headless = True
browser = webdriver.Chrome(options=option)

link_1 = 'https://www.ok.ru'

#-----------------------
path_login = '/html/body/div[10]/div[5]/div[3]/div[1]/div/div/div/div[1]/div[3]/div/div/div/div/div/div/div[1]/div[2]/div/div[2]/div[2]/div[1]/form/div[1]/div/input'
path_password = '/html/body/div[10]/div[5]/div[3]/div[1]/div/div/div/div[1]/div[3]/div/div/div/div/div/div/div[1]/div[2]/div/div[2]/div[2]/div[1]/form/div[2]/div/input'
path_btn = '/html/body/div[10]/div[5]/div[3]/div[1]/div/div/div/div[1]/div[3]/div/div/div/div/div/div/div[1]/div[2]/div/div[2]/div[2]/div[1]/form/div[4]/input'

#-----------------------
login = ''
password = ''

#-----------------------
print('go to site')

browser.get(link_1)

time.sleep(1)

browser.find_element_by_xpath(path_login).send_keys(login)

browser.find_element_by_xpath(path_password).send_keys(password)

browser.find_element_by_xpath(path_btn).click()

print('log in')

time.sleep(2)

print('start visiting')

i = 0

with open('file/users.txt', 'r') as file:
    for link in file:
        i += 1
        print(f'{i} : {link}')
        browser.get(link)
        time.sleep(4)

print('everything is successful')
print('exit after 30 seconds')
browser.quit()