from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import getpass
import time


class twitter_bot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/login')
        time.sleep(3)
        email = bot.find_element_by_class_name('js-username-field')
        password = bot.find_element_by_class_name('js-password-field')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        time.sleep(2)
        password.send_keys(self.password)
        time.sleep(2)
        bot.find_element_by_class_name("EdgeButtom--medium").click()
        time.sleep(3)


    def like_tweet(self, hastag):
        bot = self.bot
        bot.get('https://twitter.com/search?q=' + hastag + '&src=typd')
        bot.implicitly_wait(3)
        for i in range(0, 30):
            bot.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            time.sleep(10)
            tweets = bot.find_elements_by_class_name('tweet')
            links = [element.get_attribute('data-permalink-path') for element in tweets]
        for link in links:
            bot.get('https://twitter.com/' + link)
            try:
                bot.find_element_by_class_name('HeartAnimation').click()
                time.sleep(10)
            except Exception as ex:
                time.sleep(60)


if __name__ == '__main__':
    username = input('Email: ')
    password = getpass.getpass('Password: ')
    search = input('Please enter keyword: ')
    user = twitter_bot(username, password)
    user.login()
    time.sleep(10)
    user.like_tweet(search)
