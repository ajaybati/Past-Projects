from selenium import webdriver
from time import sleep

class InstaBot:
    def __init__(self, username, pw):
        self.driver = webdriver.Chrome()

        self.driver.get("https://www.messenger.com/")




        self.driver.find_element_by_xpath("//input[@name=\"email\"]").send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"pass\"]").send_keys(pw)

        self.driver.find_element_by_xpath('//button[@type="submit"]').click()
        try:

            for x in range(1):
                self.driver.find_element_by_xpath('//a[@title="Send a Like"]').click()
                sleep(0.1)
        except Exception as e:
            pass
        print("success")

        sleep(2000)

InstaBot('5109531173', 'Ajay@0819')
