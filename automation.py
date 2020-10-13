from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_browser = webdriver.Chrome('./chromedriver')

chrome_browser.get('https://www.selenium.dev/')

def sleep(num):
	time.sleep(num)

projects = chrome_browser.find_element_by_link_text('Projects')
sleep(2)
projects.click()

scrl = chrome_browser.find_element_by_tag_name('html')
sleep(2)
scrl.send_keys(Keys.END)
sleep(2)
scrl.send_keys(Keys.HOME)
sleep(2)

support = chrome_browser.find_element_by_link_text('Support')
sleep(2)
support.click()

scrl2 = chrome_browser.find_element_by_tag_name('html')
sleep(2)
scrl2.send_keys(Keys.END)
sleep(2)
scrl2.send_keys(Keys.HOME)
sleep(2)

learn_more = chrome_browser.find_element_by_link_text('LEARN MORE')
sleep(2)
learn_more.click()
print('sponsers rendered')

sponsers = chrome_browser.find_element_by_class_name('backer-logo')
sleep(2)
chrome_browser.execute_script("arguments[0].scrollIntoView();",sponsers)
sleep(2)
sponsers.click()
blog = chrome_browser.find_element_by_xpath('//*[@id="block-secondarynavigation"]/ul/li[1]/a')
sleep(2)
blog.click()

ios_i4 = chrome_browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div[3]/div/div/div[2]/div[2]/div/div/div[1]/article/div/h3/a/span')
sleep(2)
chrome_browser.execute_script("arguments[0].scrollIntoView();",ios_i4)
ios_i4.click()
sleep(2)
search = chrome_browser.find_element_by_xpath('//*[@id="edit-keys"]')
search.send_keys('automation')
search.send_keys(Keys.ENTER)
print('searching ....')

automation_link = chrome_browser.find_element_by_xpath('//*[@id="block-perfecto-content"]/div/div/div/div/div/div/div[4]/article/h2/a/span')
sleep(2)
chrome_browser.execute_script("arguments[0].scrollIntoView();",automation_link)
automation_link.click()
print(automation_link)
sleep(2)
reccomened_post = chrome_browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div[2]/h2')
chrome_browser.execute_script("arguments[0].scrollIntoView();",reccomened_post)
sleep(2)

chrome_browser.get('https://www.perfecto.io/blog/test-impact-analysis')
print('here')
sleep(2)
test_link = chrome_browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div[2]/div/div/div/div/div/div[2]/article/div/h3/a/span')
print('donee')
sleep(2)


chrome_browser.get('https://www.google.com/')
yt_searchs = chrome_browser.find_elements_by_css_selector('input[name=q]')
for yt_search in yt_searchs:
 	yt_search.send_keys('Automation In Python')

 	yt_search.send_keys(Keys.ENTER)

print('all goooood')
sleep(3)
#link = chrome_browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
chrome_browser.execute_script("window.open('https://www.youtube.com/watch?v=f7LEWxX4AVI', 'new window')")
#chrome_browser.get('https://www.youtube.com/watch?v=f7LEWxX4AVI')
sleep(2)
print('goooooood')
sleep(5)

print('finished')
#safari_browser = webdriver.Safari()
#print(safari_browser)
#safari_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')
#print('Automation access granted')

#firefox_browser = webdriver.Firefox()
#print(firefox_browser)
#firefox_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')
#print('Automation access granted')
