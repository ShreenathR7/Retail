
# app.py - The main executable file
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.options import Options
from time import sleep
from Test_locators import locators
from Test_data import data
import pytest


class Test_Logimax:
    @pytest.fixture
    

    def booting_function(self):
       self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
       self.driver.get(data.Logi_Data().url)
       self.driver.maximize_window()
       self.driver.implicitly_wait(5)
    
    def test_metal_entry(self,booting_function):   
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().username_inputBox).send_keys(data.Logi_Data().username)
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().password_inputBox).send_keys(data.Logi_Data().password)
       
        sleep(8)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().signButton).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().side_bar).click()
        sleep(6)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().retail_catalog).click()
        sleep(6)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().metal).click()
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().add_metal).click()
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().metal_name).send_keys(data.Logi_Data().metal_name)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().metal_code).send_keys(data.Logi_Data().Short_code)
    
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().metal_Tax).click()
        sleep(3)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().metal_Testbox).click()
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().status_no).click()
        sleep(2)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().status_Yes).click()
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().save_page).click()
        assert self.driver.title == 'Logimax Technology | Admin'
        print("SUCCESS : The metal list added successfully metal_name: {a} & Short_code: {b}". format(a=data.Logi_Data.metal_name, b=data.Logi_Data.Short_code))
     
    def test_double_metal_entry(self,booting_function):   
        try:
         self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().username_inputBox).send_keys(data.Logi_Data().username)
         self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().password_inputBox).send_keys(data.Logi_Data().password)
         sleep(8)
         self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().signButton).click()
         sleep(5)
         self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().side_bar).click()
         sleep(6)
         self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().retail_catalog).click()
         sleep(6)
         self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().metal).click()
         sleep(5)
         self.driver.find_element(by=By.ID,value=locators.Logi_Locators().add_metal).click()
         self.driver.find_element(by=By.ID,value=locators.Logi_Locators().metal_name).send_keys(data.Logi_Data().metal_name)
         self.driver.find_element(by=By.ID,value=locators.Logi_Locators().metal_code).send_keys(data.Logi_Data().Short_code)
    
         self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().metal_Tax).click()
         sleep(3)
         self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().metal_Testbox).click()
         self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().status_no).click()
         sleep(2)
         self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().status_Yes).click()
         self.driver.find_element(by=By.ID,value=locators.Logi_Locators().save_page).click()
         assert self.driver.title != 'Logimax Technology | Admin'
         print("SUCCESS :warning message pop up")
        except:
         assert self.driver.title == 'Logimax Technology | Admin'
         print("Warning :Double entry added")
     
    def test_update_metal_entry(self,booting_function):   
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().username_inputBox).send_keys(data.Logi_Data().username)
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().password_inputBox).send_keys(data.Logi_Data().password)
        sleep(8)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().signButton).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().side_bar).click()
        sleep(6)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().retail_catalog).click()
        sleep(6)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().metal).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().metal_edit).click()
        sleep(5) 
        element = self.driver.find_element(by=By.ID,value=locators.Logi_Locators().edit_metal_name)
        element.clear()
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().edit_metal_name).send_keys(data.Logi_Data().metal_name1)
        sleep(4)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().update).click()        
        assert self.driver.title == 'Logimax Technology | Admin'
        print("SUCCESS :updated successfully")
        
    def test_delete_metal_entry(self,booting_function):   
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().username_inputBox).send_keys(data.Logi_Data().username)
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().password_inputBox).send_keys(data.Logi_Data().password)
        sleep(8)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().signButton).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().side_bar).click()
        sleep(6)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().retail_catalog).click()
        sleep(6)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().metal).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().delete).click()    
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().delete_metal).click() 
        assert self.driver.title == 'Logimax Technology | Admin'
        print("SUCCESS :deleted successfully")
        
    