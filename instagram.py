from selenium import webdriver
import time
import username_password as up

class Browser:
    def __init__(self, link):
        self.link = link
        self.browser = webdriver.Firefox()
        Browser.openInstagram(self)

    def openInstagram(self):
        self.browser.get(self.link)
        time.sleep(2)
        Browser.loginToAccount(self)
        Browser.getFollowers(self)

    def loginToAccount(self):
        username = self.browser.find_element_by_name("username")
        password = self.browser.find_element_by_name("password")
        
        username.send_keys(up.username)
        password.send_keys(up.password)

        loginButton = self.browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button/div")
        loginButton.click()
        time.sleep(4)

        self.browser.get(self.link + "/" + up.username)
        time.sleep(3)
