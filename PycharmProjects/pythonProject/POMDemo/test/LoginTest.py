import time
from selenium import webdriver
import unittest

from POMDemo.pages.LoginPage import LoginPage
from POMDemo.pages.IndexPage import IndexPage


class LoginTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="/Users/darwoft/PycharmProjects/pythonProject/Selenium/Drivers/chromedriver")
        cls.driver.get("https://automationteststore.com/")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_Valid_Login(self):
        self.driver.find_element_by_link_text("Login or register").click()
        login = LoginPage(self.driver)
        index = IndexPage(self.driver)
        login.login("admin123", "admin")
        time.sleep(2)
        assert index.getText() == "Welcome back ramon"
        print("Valid Login")

    def test_Invalid_User_Pass(self):
        self.driver.find_element_by_link_text("Login or register").click()
        login = LoginPage(self.driver)
        login.login("usuario","pass")
        login.checkError1(self.driver,10)
        print("Error: Incorrect login or password provided.")

    def test_Empty_User(self):
        self.driver.find_element_by_link_text("Login or register").click()
        login = LoginPage(self.driver)
        login.login("", "pass")
        login.checkError1(self.driver, 10)
        print("Error: Incorrect login or password provided.")


    def test_Empty_Pass(self):
        self.driver.find_element_by_link_text("Login or register").click()
        login = LoginPage(self.driver)
        login.login("usuario", "")
        time.sleep(2)
        login.checkError1(self.driver, 10)
        print("Error: Incorrect login or password provided.")

    def test_Create_Account(self):
        self.driver.find_element_by_link_text("Login or register").click()
        login = LoginPage(self.driver)
        login.createAnAccount(self.driver, 10)
        print("usuario es Create Account page")




    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")


