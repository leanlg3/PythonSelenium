from selenium.webdriver import ActionChains


def moveTo(self, xpath):
        # object of ActionChains
        a = ActionChains(self.driver)
        # hover over element
        a.move_to_element(xpath).perform()



