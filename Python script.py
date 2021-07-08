from selenium import webdriver
import time

web = webdriver.Chrome()
web.get('https://bettin.gs/login')

time.sleep(1)

Email = 'shihongfoo@gmail.com'
typeEmail = web.find_element_by_xpath('//*[@id="email"]')
typeEmail.send_keys(Email)

Password = "06011712Fsh"
typePassword = web.find_element_by_xpath('//*[@id="password"]')
typePassword.send_keys(Password)

Login = web.find_element_by_xpath('//*[@id="loginForm"]/div[2]/div/p/input')
Login.click()
                                    
