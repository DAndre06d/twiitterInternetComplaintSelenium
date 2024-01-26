import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

user_agent = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
              "Chrome/120.0.0.0 Safari/537.36")
TWITTER_USERNAME = os.environ.get("TWIT_USERNAME")
TWITTER_PASSWORD = os.environ.get("TWIT_PASS")


class InternetSpeedTwitterBot:
    def __init__(self):
        self.chrome_options = Options()
        self.chrome_options.add_experimental_option("detach", True)
        self.chrome_options.add_argument(f"user-agent={user_agent}")
        self.chrome_options.add_argument("accept-language=en-US,en;q=0.9")
        self.chrome_options.add_argument("start-maximized")
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        """
        Opens and read the internet speed, Returns the download speed and upload speed in a list, in the position[0]
        it contains the download speed, position[1] has the upload speed
        """
        self.driver.get("https://www.speedtest.net/")
        go = self.driver.find_element(By.CLASS_NAME, "start-text")
        go.click()
        time.sleep(43)
        speed = []
        self.down = self.driver.find_element(By.XPATH, "//*[@id='container']/div/div[3]/div/div/div/div[2]"
                                                       "/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div"
                                                       "/div[2]/span").text
        self.up = self.driver.find_element(By.XPATH, "//*[@id='container']/div/div[3]/div/div/div/"
                                                     "div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div"
                                                     "[1]/div[2]/div/div[2]/span").text
        speed.append(float(self.down))
        speed.append(float(self.up))
        return speed

    def tweet_at_provider(self, message):
        """Opens the Twitter website and log the user in and writes the complaint and post it"""
        self.driver.get("https://twitter.com/")
        time.sleep(1.5)
        sign_in = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div'
                                                     '/div/div[1]/div[1]/div/div[3]/div[5]/a/div')
        sign_in.click()
        time.sleep(1.5)
        inputs = self.driver.find_element(By.NAME, 'text')
        inputs.send_keys(TWITTER_USERNAME)
        nexts = self.driver.find_element(By.XPATH, "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]"
                                                   "/div/div/div[2]/div[2]/div/div/div/div[6]")
        nexts.click()
        time.sleep(2)
        password = self.driver.find_element(By.NAME, "password")
        password.send_keys(TWITTER_PASSWORD)
        login = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div'
                                                   '[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div')
        login.click()
        time.sleep(5)
        # get_started = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]'
        #                                                  '/div[2]/div/div[2]/div/div[2]/div[2]/div')
        # get_started.click()
        # get_started_close = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div'
        #                                                        '/div[2]/div[2]/div/div/div[2]/div[1]/div/div/div/div'
        #                                                        '/div[1]/div')
        # get_started_close.click()
        input_field = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div'
                                                         '/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]'
                                                         '/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]'
                                                         '/div/div/div/div/div/div[2]/div')
        input_field.send_keys(message)
        self.driver.quit()



