import time
import unittest
from selenium import webdriver

from POMDemo.pages.IndexPage import IndexPage
from POMDemo.pages.LoginPage import LoginPage


class ShopPageTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="/Users/darwoft/PycharmProjects/pythonProject/Selenium/Drivers/chromedriver")
        cls.driver.get("https://automationteststore.com/")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()



    def test_Buy_Shoes(self):
        login = LoginPage(self.driver)
        shop = IndexPage(self.driver)
        self.driver.find_element_by_link_text("Login or register").click()
        login.login("admin123", "admin")
        time.sleep(2)
        shop.openApperalandAccesories()
        shop.checkText(self.driver,10)





