import time

import allure
from allure_commons.types import AttachmentType

from PageObject.test_pages_orangehrm import Test_ohrm_login
from PageObject.test_add_emp_pages import Test_Add_Emp
from PageObject.test_search_emp_pages import Test_Search_Emp
from utilities.logger import LogGenerator
from utilities.ReadConfig import ReadConfig

class Test_searchch_empemp():
    Username = ReadConfig.getUserName()
    Password = ReadConfig.getPassword()

    log= LogGenerator.logger()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.link("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    @allure.title("TITLE OF TEST CASE IS #3")
    @allure.issue("THIS IS THE ISSUE #3")
    @allure.story("THIS IS A STORY #3")

    def test_search_emp_004(self,setup):
        self.driver=setup

        self.obj= Test_ohrm_login(self.driver)

        self.log.info("TESTCASE TEST_SEARCH_EMP_004 IS STARTED")

        self.log.info("OPEN THE BROWSER")

        self.log.info("MAXIMIZE THE BROWSER")

        self.log.info("NAVIGATING TO URL")
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        self.log.info("ENTERING THE USERNAME")
        self.obj.test_enter_username(self.Username)

        self.log.info("ENTERING THE PASSWORD")
        self.obj.test_enter_password(self.Password)

        self.log.info("CLICK ON LOGIN BUTTON")
        self.obj.test_click_login()

        self.obj2= Test_Add_Emp(self.driver)

        self.log.info("CLICK ON PIM BUTTON")
        self.obj2.test_click_pim_tab()

        self.obj3=Test_Search_Emp(self.driver)

        self.log.info("CLICK ON EMPID BUTTON")
        self.obj3.test_enter_search_emp("0565")

        self.log.info("CLICK ON SEARCH BUTTON")
        self.obj3.test_click_search_button()

        time.sleep(3)

        print("DETAILS OF ADDED EMPLOYEE ARE FOLLOWING ")
        if(self.obj3.test_search_result()==True):
            allure.attach(self.driver.get_screenshot_as_png(), name="test_search_emp_004_pass",attachment_type=AttachmentType.PNG)
            self.log.info("DETAILS OF EMPLOYEE ARE PRINTED")
            self.log.info("TAKING THE SCREENSHOT")
            self.log.info("TEST CASE IS PASSED")
            self.driver.save_screenshot("C:\\Users\\lenovo\\PycharmProjects\\OrangeHRM_project\\screenshot\\test_search_emp_004.pass.png")


        else:

            allure.attach(self.driver.get_screenshot_as_png(), name="test_search_emp_004-pass",
                          attachment_type=AttachmentType.PNG)
            self.log.info("TEST CASE IS FAILED")
            self.driver.save_screenshot("C:\\Users\\lenovo\\PycharmProjects\\OrangeHRM_project\\screenshot\\test_search_emp_004.fail.png")
            assert False;
        self.log.info("TESTCASE TEST_SEARCH_EMP_004 IS COMPLETED")