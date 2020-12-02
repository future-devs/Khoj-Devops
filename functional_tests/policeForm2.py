# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Test1(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('functional_tests/chromedriver.exe')
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_1(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/police/get_upload_lost_person_image_form")
        driver.find_element_by_xpath("//form[@id='lost_person_details']/div/center").click()
        driver.find_element_by_name("first_name").click()
        driver.find_element_by_name("first_name").clear()
        driver.find_element_by_name("first_name").send_keys("Astitva")
        driver.find_element_by_name("last_name").click()
        driver.find_element_by_name("last_name").clear()
        driver.find_element_by_name("last_name").send_keys("Singhal")
        driver.find_element_by_id("gender").click()
        driver.find_element_by_id("gender").click()
        driver.find_element_by_name("blood_group").click()
        driver.find_element_by_name("blood_group").clear()
        driver.find_element_by_name("blood_group").send_keys("A+")
        driver.find_element_by_id("face_complexion").click()
        driver.find_element_by_id("face_complexion").click()
        driver.find_element_by_id("body_built").click()
        driver.find_element_by_id("body_built").click()
        driver.find_element_by_name("lower_height_range").click()
        driver.find_element_by_name("lower_height_range").clear()
        driver.find_element_by_name("lower_height_range").send_keys("800")
        driver.find_element_by_name("upper_height_range").click()
        driver.find_element_by_name("upper_height_range").clear()
        driver.find_element_by_name("upper_height_range").send_keys("1000")
        driver.find_element_by_id("lost_person_name").click()
        driver.find_element_by_id("lost_person_name").clear()
        driver.find_element_by_id("lost_person_name").send_keys("5199asaassaasa")
        driver.find_element_by_name("face_shape").click()
        Select(driver.find_element_by_name("face_shape")).select_by_visible_text("Heart")
        driver.find_element_by_name("face_shape").click()
        driver.find_element_by_id("last_appearence_place").click()
        Select(driver.find_element_by_id("last_appearence_place")).select_by_visible_text("Jamia Nagar")
        driver.find_element_by_id("last_appearence_place").click()
        driver.find_element_by_id("search_button").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
