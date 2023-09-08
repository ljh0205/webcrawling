'''from selenium import webdriver
driver1=webdriver.Chrome()
driver1.get('http)
driver1.set_window_size(960,540)
driver1.set_window_position(960,540)


driver2=webdriver.Chrome()
driver2.get()
driver2.set_window_size(960,540)
driver2.set_window_position(0,0)


driver3=webdriver.Chrome()
driver3.get()
driver3.set_window_size(960,540)
driver3.set_window_position(0,540)       


driver4=webdriver.Chrome()
driver4.get()
driver4.set_window_size(960,540)
driver4.set_window_position(960,0)       



from selenium import webdriver
u=['https://naver.com','https://google.com','https://youtube.com','https://daum.net']
d=[]
import time
w=1920/2
h=1080/2
p=[(0,0),(w,0),(0,h),(w,h)]
for i in range(4):
    driver=webdriver.Chrome()
    d.append(driver)
    d[i].get(u[i])
    d[i].set_window_size(w,h)
    d[i].set_window_position(p[i][0],p[i][1])
    time.sleep(2)


'''
'''
#셀레니움 콘솔창 숨기기

from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from subprocess import CREATE_NO_WINDOW

s=Service()
s.creation_flags=CREATE_NO_WINDOW

driver=webdriver.Chrome(service=s)
driver.get("https://sbasu.pythonanywhere.com/tastyFoodApp/")


p='//*[@id="homePageLinks"]/ul/li/a'
e=driver.find_element(by='xpath',value=p)
e.click()

p='//*[@id="id_firstName"]'
e=driver.find_element('xpath',p)
e.send_keys('juho')

p='//*[@id="id_lastName"]'
e=driver.find_element('xpath',p)
e.send_keys('juho') 

p='//*[@id="id_gender"]/li[1]/label'
e=driver.find_element('xpath',p)
e.click()

p='//*[@id="id_username"]'
e=driver.find_element('xpath',p)
e.send_keys('juho') 

p='//*[@id="id_password"]'
e=driver.find_element('xpath',p)
e.send_keys('1234') 

p='//*[@id="id_state"]'
e=driver.find_element('xpath',p)
e.click()

p='//*[@id="id_fee"]'
e=driver.find_element('xpath',p)
e.click()

p='//*[@id="id_date"]'
e=driver.find_element('xpath',p)
e.send_keys('09/01/2023')

p='//*[@id="id_state"]/option[2]'
e=driver.find_element('xpath',p)
e.click()

p='//*[@id="id_fee"]/option[3]'
e=driver.find_element('xpath',p)
e.click()

p='/html/body/form/div/input'
e=driver.find_element('xpath',p)
e.click()


from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from subprocess import CREATE_NO_WINDOW

s=Service()
s.creation_flags=CREATE_NO_WINDOW

driver=webdriver.Chrome(service=s)
driver.get("http://www.google.com")

p='//*[@id="APjFqb"]'
e=driver.find_element('xpath',p)
e.send_keys('세종 도담초등학교')

from selenium.webdriver.common.keys import Keys
e.send_keys(Keys.RETURN)
'''

from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from subprocess import CREATE_NO_WINDOW

import time

s=Service()
s.creation_flags=CREATE_NO_WINDOW

driver=webdriver.Chrome(service=s)
driver.get("http://www.youtube.com")

time.sleep(3)

##p='//*[@id="search-form"]'
##e=driver.find_element('xpath',p)
##e.click()
##
##time.sleep(3)

p='//*[@id="search-form"]'
e=driver.find_element('xpath',p)
e.send_keys('스포티비')

time.sleep(3)
##
##p='//*[@id="search-icon-legacy"]'
##e=driver.find_element('xpath',p)
##e.click()














