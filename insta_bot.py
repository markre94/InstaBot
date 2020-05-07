from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from secret import my_secret_password


class Instabot:
    def __init__(self):
        self.browser = webdriver.Chrome()
        self.browser.get('https://www.instagram.com/')
        time.sleep(1)

    def refresh_page(self):
        browser = self.browser
        browser.refresh()

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

    def someones_page(self, username: str):
        browser = self.browser
        browser.get('https://www.instagram.com/' + username)
        time.sleep(3)

    def open_photo(self):
        browser = self.browser
        photo = browser.find_element_by_class_name('_9AhH0')
        photo.click()
        time.sleep(3)

    def like_photo(self):
        browser = self.browser
        like_button = browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]')
        like_button.click()
        time.sleep(1)

    def post_comment(self, commentary):
        browser = self.browser
        # CLick on a text bar
        comment_space = browser.find_element_by_class_name('Ypffh')
        comment_space.click()
        # Enter the comment
        browser.find_element_by_xpath(
            '/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/textarea').send_keys(commentary)
        browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/button').click()
        pass

    def count_posts(self):
        browser = self.browser
        post_count = browser.find_element_by_class_name('g47SY').text
        return int(post_count.replace(' ', ''))
        pass


if __name__ == '__main__':
    bot1 = Instabot()
    bot1.login('krezel94', my_secret_password)
    bot1.someones_page('krezel94')
    current_number = bot1.count_posts()
    time.sleep(3)

    # Check for the new added photos

    while True:
        time.sleep(3)
        new_number = bot1.count_posts()
        if new_number == current_number:
            time.sleep(5)
            bot1.refresh_page()
        else:
            time.sleep(1)
            bot1.open_photo()
            bot1.like_photo()
            bot1.post_comment('<3')
            time.sleep(1)
            break

    # bot1.open_photo()
    # bot1.like_photo()
    # bot1.post_comment('Keep up a good work!')
    pass
