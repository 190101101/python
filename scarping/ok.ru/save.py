from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

option = webdriver.ChromeOptions()
option.headless = True
driver = webdriver.Chrome(options=option)

link_1 = 'https://www.ok.ru'
link_2 = 'https://ok.ru/dk?st.cmd=searchResult&st.mode=Users&st.grmode=Groups&st.gender=f&st.location=%D0%91%D0%B0%D0%BA%D1%83&st.country=10410450732&st.cityId=10393008051&st.single=on&st.onSite=on&st.fromAge=20&st.tillAge=30'

#-----------------------
path_login = '/html/body/div[10]/div[5]/div[3]/div[1]/div/div/div/div[1]/div[3]/div/div/div/div/div/div/div[1]/div[2]/div/div[2]/div[2]/div[1]/form/div[1]/div/input'
path_password = '/html/body/div[10]/div[5]/div[3]/div[1]/div/div/div/div[1]/div[3]/div/div/div/div/div/div/div[1]/div[2]/div/div[2]/div[2]/div[1]/form/div[2]/div/input'
path_btn = '/html/body/div[10]/div[5]/div[3]/div[1]/div/div/div/div[1]/div[3]/div/div/div/div/div/div/div[1]/div[2]/div/div[2]/div[2]/div[1]/form/div[4]/input'

#-----------------------
login = ''
password = ''

#-----------------------
print('go to site')

driver.get(link_1)

time.sleep(1)

driver.find_element_by_xpath(path_login).send_keys(login)

driver.find_element_by_xpath(path_password).send_keys(password)

driver.find_element_by_xpath(path_btn).click()

print('log in')

time.sleep(1)

print('go to the site now')


print('go down so that all users are visible')


driver.get(link_2)

print('window scroll begin');

time.sleep(1)

for i in range(100):
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(0.3)

driver.execute_script('window.scrollTo(0, 0)')

time.sleep(2)

path_wrap = '/html/body/div[10]/div[5]/div[5]/div[1]/div/div[2]/div[1]/div[3]/div[2]/div/div/div[3]/div/div/portal-search/div/div[1]/div[2]/div/div[2]'

elements = []
elementss = []
links = []

print('looking for x-pat content')

elements = driver.find_elements_by_class_name('photo-link__79ad9')
tags = list(set(elements)) 

print('started collecting data')

i = 0
for element in tags:
    i += 1
    href = element.get_attribute('href')[:34]
    print(f'{i} : {href}')
    links.append(element.get_attribute('href')[:34])

print('collect data')

new_links = list(set(links))
print('write data to file')

with open('file/users.txt', 'w') as file:
    for link in new_links:
        file.write(link+'\n')

print('everything is successful')
print('exit after 2 seconds')
time.sleep(2)
driver.quit()