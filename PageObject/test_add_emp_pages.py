import time

from selenium.webdriver.common.by import By
from pynput.keyboard import Controller,Key
from selenium.common import NoSuchElementException


class Test_Add_Emp():
    pim_tab_xp = (By.XPATH,"//span[text()='PIM']")
    add_button_xp =(By.XPATH,'//i[@class="oxd-icon bi-plus oxd-button-icon"]')
    firstname_tf_xp= (By.XPATH,'//input[@name="firstName"]')
    middlename_tf_xp=(By.XPATH,'//input[@name="middleName"]')
    lastname_tf_xp = (By.XPATH,'//input[@name="lastName"]')
    upload_icon_xp = (By.XPATH,'//i[@class="oxd-icon bi-plus"]')
    save_button_xp =(By.XPATH,'//button[@type="submit"]')
    success_msg_xp=(By.XPATH,"//div[@class='oxd-toast-container oxd-toast-container--bottom']")
    get_id_xp = (By.XPATH,'/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/input[1]')

    def __init__(self,driver):
        self.driver=driver

    def test_click_pim_tab(self):
        self.driver.find_element(*Test_Add_Emp.pim_tab_xp).click()

    def test_add_button_xp(self):
        self.driver.find_element(*Test_Add_Emp.add_button_xp).click()

    def test_add_firstname(self,firstname):
        self.driver.find_element(*Test_Add_Emp.firstname_tf_xp).send_keys(firstname)

    def test_add_middlename(self,middlename):
        self.driver.find_element(*Test_Add_Emp.middlename_tf_xp).send_keys(middlename)

    def test_add_lastname(self,lastname):
        self.driver.find_element(*Test_Add_Emp.lastname_tf_xp).send_keys(lastname)

    def test_get_emp_id_value(self):
        emp_id123=self.driver.find_element(*Test_Add_Emp.get_id_xp).get_attribute("value")
        print("\n Employee ID ",emp_id123)

    def test_upload_image(self):
        self.driver.find_element(*Test_Add_Emp.upload_icon_xp).click()
        time.sleep(3)
        keyboard=Controller()
        keyboard.type("C:\\Users\\lenovo\\PycharmProjects\\OrangeHRM_project\\testdata\\photo_shivaji_maharaj.jpeg")
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(2)

    def test_click_save_button(self):
        self.driver.find_element(*Test_Add_Emp.save_button_xp).click()
        time.sleep(3)

    def test_print_success_msg(self):
        try:
            success_msg = self.driver.find_element(*Test_Add_Emp.success_msg_xp).text
            print("\n TEXT AFTER ADDING EMPLOYEE")
            print("\n", success_msg)
            return True
        except NoSuchElementException:
            return False







