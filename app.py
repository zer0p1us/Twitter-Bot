from selenium import webdriver #to get the browser 
from selenium.webdriver.common.keys import Keys #to send key to browser
import getpass #to get password safely
import time #to pause the program

#a calss to store all twetter related objects and functions
class twitter_bot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    #login function
    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/login')
        #sleep to wait for the browser to get the website
        time.sleep(3)
        email = bot.find_element_by_class_name('js-username-field') #get the email field
        password = bot.find_element_by_class_name('js-password-field') #get the password field
        
        #clear the email and password field just in case of autofill
        email.clear()
        password.clear()
        
        #fill in email field
        email.send_keys(self.username) 
        time.sleep(2)
        
        #fill in password field
        password.send_keys(self.password) 
        time.sleep(2)
        
        #click the login button
        bot.find_element_by_class_name("EdgeButtom--medium").click()
        time.sleep(3)


    def like_tweet(self, search):
        bot = self.bot
        #use keyword to search
        bot.get('https://twitter.com/search?q=' + search + '&src=typd')
        bot.implicitly_wait(3)
        #get posts
        for i in range(0, 30):
            bot.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            time.sleep(10)
            tweets = bot.find_elements_by_class_name('tweet')
            links = [element.get_attribute('data-permalink-path') for element in tweets]
        #like posts
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
