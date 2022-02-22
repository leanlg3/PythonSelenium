from telnetlib import EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from POMDemo.utils.Utility import moveTo


class IndexPage:
    def __init__(self, driver):
        self.driver = driver
        self.accountTitle = "//div[contains(@class,'menu_text')]"
        self.apparelXpath = "//*[@id='categorymenu']/nav/ul/li[2]/a"
        self.shoesXpath = "//*[@id='categorymenu']/nav/ul/li[2]/div/ul[1]/li[1]/a"

    def getText(self):
       return self.driver.find_element_by_xpath(self.accountTitle).text

    def openApperalandAccesories(self):
        shoes = self.driver.find_element_by_xpath(self.apparelXpath)
        moveTo(self, shoes)
        self.driver.find_element_by_xpath(self.shoesXpath).click()

    def checkText(self,driver,time):
        element = WebDriverWait(driver, time).until(EC.element_to_be_clickable((By.XPATH, self.shoesXpath)))
        return element





