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
        self.browser.refresh()

    def login(self, username: str, passwd: str):
        self.browser.find_element_by_name("username").send_keys(username)
        my_passwd = self.browser.find_element_by_name("password")
        my_passwd.send_keys(passwd)
        my_passwd.send_keys(Keys.ENTER)
        time.sleep(3)

    def open_someones_page(self, username: str):
        self.browser.get('https://www.instagram.com/' + username)
        time.sleep(3)

    def open_post(self):
        photo = self.browser.find_element_by_class_name('_9AhH0')
        photo.click()
        time.sleep(3)

    def like_photo(self):
        like_button = self.browser.find_element_by_xpath(
            '/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]')
        like_button.click()
        time.sleep(1)

    def post_comment(self, commentary):
        # CLick on a text bar
        comment_space = self.browser.find_element_by_class_name('Ypffh')
        comment_space.click()
        # Enter the comment
        self.browser.find_element_by_xpath(
            '/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/textarea').send_keys(commentary)
        self.browser.find_element_by_xpath(
            '/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/button').click()

    def count_posts(self):
        post_count = self.browser.find_element_by_class_name('g47SY').text
        return int(post_count.replace(' ', ''))

    def check_for_added_post(self):
        current_number = self.count_posts()
        while True:
            time.sleep(3)
            new_number = self.count_posts()
            if new_number == current_number:
                time.sleep(5)
                self.refresh_page()
            elif new_number > current_number:
                time.sleep(1)
                self.open_post()
                self.like_photo()
                self.post_comment('The bot was here.')
                time.sleep(1)
                break


# meetoda check_if_changed -> bool

if __name__ == '__main__':
    bot1 = Instabot()
    bot1.login('krezel94', my_secret_password)
    bot1.open_someones_page('krezel94')
    time.sleep(3)
    bot1.check_for_added_post()
