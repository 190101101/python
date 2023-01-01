import time
from pyvirtualdisplay import Display
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument('--profile-directory=Default')
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-plugins-discovery");
chrome_options.add_argument("--start-maximized")

browser = webdriver.Chrome(chrome_options=chrome_options)
browser.delete_all_cookies()
browser.set_window_size(1280,980)
browser.set_window_position(0,0)

browser.get('https://10fastfingers.com/login')

path_log = '/html/body/div[4]/div/div[4]/div/div[1]/div/div[2]/div/div[2]/form/div[3]/input'
path_pass = '/html/body/div[4]/div/div[4]/div/div[1]/div/div[2]/div/div[2]/form/div[4]/input'
path_btn = '/html/body/div[4]/div/div[4]/div/div[1]/div/div[2]/div/div[2]/form/button'
path_input = '/html/body/div[4]/div/div[4]/div[1]/div[1]/div[7]/div[2]/div/div[1]/input'
path_not = '/html/body/div[2]/div/nav/div[2]/ul[4]/li[2]/span[1]/a'
path_not_href = '/html/body/div[3]/div/div/div[2]/ul/li[1]/a'
path_test = '/html/body/div[4]/div[1]/div[4]/div[1]/div/div[1]/table/tbody/tr[1]/td[1]/a'
path_start = '/html/body/div[4]/div[1]/div[4]/div[1]/div/div[3]/div[1]/button'

browser.find_element_by_xpath(path_log).send_keys('orxan_shirinov_1991@mail.ru')
browser.find_element_by_xpath(path_pass).send_keys('alloverme')
browser.find_element_by_xpath(path_btn).click()

i = 1

while i < 384:
    
    word = browser.find_element_by_xpath('/html/body/div[4]/div/div[4]/div[1]/div[1]/div[7]/div[1]/div/span['+ str(i) +']')

    i += 1

    browser.find_element_by_xpath(path_input).send_keys(word.text + " ")
    
    print(word.text)


print('бот выполнил задание')
