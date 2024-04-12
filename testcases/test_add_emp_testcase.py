import time

import allure
from allure_commons.types import AttachmentType

from PageObject.test_add_emp_pages import Test_Add_Emp
from PageObject.test_pages_orangehrm import Test_ohrm_login
from utilities.ReadConfig import ReadConfig
from utilities.logger import LogGenerator

class Test_Addd_Emp():
    USERNAME=ReadConfig.getUserName()
    PASSWORD=ReadConfig.getPassword()

    log=LogGenerator.logger()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.link("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    @allure.title("TITLE OF THE TEST CASE #2")
    @allure.issue("THIS IS THE ISSUE #2")
    @allure.story("THIS IS THE STORY #2")

    def test_add_emp_003(self,setup):
        self.driver = setup

        self.log.info("TEST CASE ADD_EMPL_003 IS STARTED")

        self.log.info("OPENING THE BROWSER")

        self.log.info("MAXIMIZE THE BROWSER")

        self.obj=Test_ohrm_login(self.driver)

        self.log.info("NAVIGATING TO THE URL")
        self.obj.test_set_url("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        self.log.info("ENTERTING THE USERNAME")
        self.obj.test_enter_username(self.USERNAME)

        self.log.info("ENTERING THE PASSWORD")
        self.obj.test_enter_password(self.PASSWORD)

        self.log.info("CLICK ON THE LOGIN BUTTON")
        self.obj.test_click_login()

        self.obj2=Test_Add_Emp(self.driver)

        self.log.info("CLICK ON THE PIM TAB")
        self.obj2.test_click_pim_tab()

        self.log.info("CLICk ON THE ADD BUTTON")
        self.obj2.test_add_button_xp()

        self.log.info("ENTERING THE USERNAME")
        self.obj2.test_add_firstname("JUNKOOK")

        self.log.info("ENTERING THE PASSWORD")
        self.obj2.test_add_middlename("KOOKIE")

        self.log.info("ENTERING THE LASTNAME")
        self.obj2.test_add_lastname("JK")

        self.log.info("UPLOAD THE DISPLAY PROFILE")
        self.obj2.test_upload_image()
        time.sleep(3)

        self.log.info("CLICK ON THE SAVE BUTTON")
        self.obj2.test_click_save_button()

        self.log.info("CHECKING FOR THE SUCCESS MESSAGE STATUS")
        if (self.obj2.test_print_success_msg() == True):
            self.log.info("TAKING SCREENSHOT")
            allure.attach(self.driver.get_screenshot_as_png(), name="add_emp_003_pass.png",
                          attachment_type=AttachmentType.PNG)
            self.driver.save_screenshot("C:\\Users\\lenovo\\PycharmProjects\\OrangeHRM_project\\screenshot\\add_emp_003_pass.png");

            assert True;

        else:
            self.log.info("TAKING SCREENSHOT")
            allure.attach(self.driver.get_screenshot_as_png(), name="add_emp_003_fail.png",
                          attachment_type=AttachmentType.PNG)
            self.driver.save_screenshot("C:\\Users\\lenovo\\PycharmProjects\\OrangeHRM_project\\screenshot\\add_emp_003_fail.png");
            assert False;

        self.log.info("TEST CASE ADD_EMP_003 IS COMPLETED")
