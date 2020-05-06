from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from secret import my_secret_password


class Instabot:
    def __init__(self):
        self.browser = webdriver.Chrome()
        self.browser.get('https://www.instagram.com/')
        time.sleep(1)

    def login(self, username: str, passwd: str):
        browser = self.browser
        browser.find_element_by_name("username").send_keys(username)
        my_passwd = browser.find_element_by_name("password")
        my_passwd.send_keys(passwd)
        my_passwd.send_keys(Keys.ENTER)
        time.sleep(3)
        # if browser.find_elements_by_xpath()
        # unclick any pop out about notfication
        browser.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]').click()

    def lebron_page(self):
        browser = self.browser
        browser.get('https://www.instagram.com/kingjames')

    def like_photo(self, commentary: str):
        browser = self.browser
        photo = browser.find_element_by_class_name('_9AhH0')
        photo.click()
        time.sleep(3)
        like_button = browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]')
        like_button.click()
        time.sleep(1)

        # CLick on a text bar
        comment_space = browser.find_element_by_class_name('Ypffh')
        comment_space.click()
        # Enter the comment
        browser.find_element_by_xpath(
            '/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/textarea').send_keys(commentary)
        browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/button').click()
        pass


if __name__ == '__main__':
    bot1 = Instabot()
    bot1.login('krezel94', my_secret_password)
    bot1.lebron_page()
    bot1.like_photo(commentary='Great post!')
    pass
