# from selenium import webdriver
# from time import sleep
# from selenium.webdriver.common.action_chains import ActionChains
#
# class InstaBot:
#     def __init__(self, username, pw):
#         self.driver = webdriver.Chrome()
#
#         self.driver.get("https://www.messenger.com/")
#
#
#
#
#         self.driver.find_element_by_xpath("//input[@name=\"email\"]").send_keys(username)
#         self.driver.find_element_by_xpath("//input[@name=\"pass\"]").send_keys(pw)
#
#         self.driver.find_element_by_xpath('//button[@type="submit"]').click()
#         # try:
#         #
#         #     for x in range(2000):
#         #         self.driver.find_element_by_xpath('//a[@title="Send a Like"]').click()
#         #         sleep(0.1)
#         # except Exception as e:
#         #     pass
#         self.driver.find_element_by_xpath("//*[@data-editor]").click()
#         actions = ActionChains(self.driver)
#         actions.send_keys('I LOVE ME SOME VERMA')
#         actions.perform()
#         print("success")
#
#         sleep(2000)
#
