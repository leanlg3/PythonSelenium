from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.username_Id = "loginFrm_loginname"
        self.password_Id = "loginFrm_password"
        self.login_btn_xpath = "//button[contains(@title,'Login')]"
        self.alert_xpath = "//*[@class ='alert alert-error alert-danger']"
        self.continue_xpath = "//button[contains(@title,'Continue')]"
        self.account_title_xpath = "//*[contains(text(),' Create Account')]"


    def login(self, username, password):
        self.driver.find_element_by_id(self.username_Id).clear()
        self.driver.find_element_by_id(self.username_Id).send_keys(username)
        self.driver.find_element_by_id(self.password_Id).clear()
        self.driver.find_element_by_id(self.password_Id).send_keys(password)
        self.driver.find_element_by_xpath(self.login_btn_xpath).click()

    def checkError1(self,driver,time):
        element = WebDriverWait(driver, time).until(EC.element_to_be_clickable((By.XPATH, self.alert_xpath)))
        return element

    def createAnAccount(self,driver,time):
        self.driver.find_element_by_xpath(self.continue_xpath).click()
        element = WebDriverWait(driver, time).until(EC.element_to_be_clickable((By.XPATH, self.account_title_xpath)))
        return element














