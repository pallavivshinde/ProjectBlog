import time

import allure
from allure_commons.types import AttachmentType
from PageObject.test_pages_orangehrm import Test_ohrm_login
from utilities.logger import LogGenerator
from utilities.ReadConfig import ReadConfig

class Test_ohrmpro():
    USERNAME =ReadConfig.getUserName()
    PASSWORD = ReadConfig.getPassword()
    log=LogGenerator.logger()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.link("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    @allure.title("TITLE OF THE TEST CASE")
    @allure.issue("THIS IS THE ISSUE #1")
    @allure.story("THIS IS A STORY #1")
    def test_page_title_001(self,setup):
        self.log.info("TEST CASE PAGE_TITLE_001 IS STARTED ")
        self.log.info("MAXIMIZE THE BROWSER")
        self.driver=setup
        self.obj=Test_ohrm_login(self.driver)

        self.log.info("NAVIGATING TO THE URL")
        self.obj.test_set_url('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
        time.sleep(12)

        self.log.info("CHECKING THE TITLE OF THE PAGE")
        if(self.driver.title=="OrangeHRM"):
            self.log.info("TAKING THE SCREENSHOT")
            self.driver.save_screenshot("C:\\Users\\lenovo\\PycharmProjects\\OrangeHRM_project\\screenshot\\test_page_title_001_pass.png")
            print("\n YOU ARE IN THE CORREECT PAGE")

            self.log.info("CLOSING THE BROWSER")
            self.driver.close()
            assert True
        else:
            self.log.info("TAKING THE SCREENSHOT")
            self.driver.save_screenshot("C:\\Users\\lenovo\\PycharmProjects\\OrangeHRM_project\\screenshot\\test_page_title_001_fail.png")
            print("\n SORRY INVALID URL")
            self.driver.close()
            assert False
        self.log.info("TEST CASE PAGE_TITLE_001 IS COMPLETED")

    def test_login_002(self,setup):
        self.log.info("TEST CASE LOGIN_002 IS STARTED")
        self.log.info("OPENING THE BROWSER")
        self.log.info("MAXIMIZE THE WINDOW")
        self.driver = setup
        self.obj= Test_ohrm_login(self.driver)

        self.log.info("NAVIGATING TO THE URL")
        self.obj.test_set_url("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        self.log.info("ENTER THE USERNAME")
        self.obj.test_enter_username('Admin')

        self.log.info("ENTER THE PASSWORD")
        self.obj.test_enter_password('admin123')

        self.log.info("CLICK ON THE LOGIN BUTTON ")
        self.obj.test_click_login()

        self.log.info("CHECKING FOR THE STATUS")
        self.obj.test_login_status()
        #
        if(self.obj.test_login_status()==True):
            self.log.info("TAKING THE SCREENSHOT")
            allure.attach(self.driver.get_screenshot_as_png(),name="test_login_002_pass" ,attachment_type=AttachmentType.PNG)
            self.driver.save_screenshot("C:\\Users\\lenovo\\PycharmProjects\\OrangeHRM_project\\screenshot\\test_page_title_002_pass.png")

            print("\n LOGIN SUCCESSFUL")

            self.log.info("CLICK ON THE MENU BUTTON")
            self.obj.test_click_menu_button()

            self.log.info("CLICK ON THE LOGOUT BUTTON")
            self.obj.test_click_logout()

            self.log.info("CLOSE THE BROWSER")
            self.driver.close()
            assert True

        else:
            self.log.info("TAKING THE SCREENSHOT")
            allure.attach(self.driver.get_screenshot_as_png(),name="test_login_002_fail" ,attachment_type=AttachmentType.PNG)
            self.driver.save_screenshot("C:\\Users\\lenovo\\PycharmProjects\\OrangeHRM_project\\screenshot\\test_page_title_002_fail.png")

            print("\n LOGIN UNSUCESSFUL")

            self.log.info("CLOSING THE BROWSER")
            self.driver.close()

            assert False


        self.log.info("TEST CASE LOGIN_002 IS COMPLETED")





