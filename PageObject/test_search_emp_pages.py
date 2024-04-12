import time

from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException

class Test_Search_Emp():

    empid_tf_xp =(By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[2]")
    search_button_xp= (By.XPATH,"//button[text()=' Search ']")
    search_result_css =(By.XPATH,"//div[@class='oxd-table-row oxd-table-row--with-border oxd-table-row--clickable']")

    def __init__(self,driver):
        self.driver=driver

    def test_enter_search_emp(self,empid):
        self.driver.find_element(*Test_Search_Emp.empid_tf_xp).send_keys(empid)
        time.sleep(3)

    def test_click_search_button(self):
        self.driver.find_element(*Test_Search_Emp.search_button_xp).click()
        time.sleep(3)

    def test_search_result(self):
        try:
            firstmiddlename=self.driver.find_element(*Test_Search_Emp.search_result_css).text
            print("\n",firstmiddlename)
            return True
        except NoSuchElementException:
            return False