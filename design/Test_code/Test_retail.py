
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
    
    
   
    def test_design(self,booting_function):
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().username_inputBox).send_keys(data.Logi_Data().username)
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().password_inputBox).send_keys(data.Logi_Data().password)
        sleep(4)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().signButton).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().side_bar).click() 
        sleep(5) 
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().retail_catalog).click()
        sleep(5)       
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().design).click()    
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().add_design).click()
        sleep(5)        
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().design_name).send_keys(data.Logi_Data().design_name)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().design_inactive).click()
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().design_active).click()
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().save_design_page).click()
        assert self.driver.title == 'Logimax Technology | Admin'
        print("SUCCESS : The design list added successfully design_name: {a}". format(a=data.Logi_Data.design_name,))
      
    def test_double_design(self,booting_function):
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().username_inputBox).send_keys(data.Logi_Data().username)
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().password_inputBox).send_keys(data.Logi_Data().password)
        sleep(4)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().signButton).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().side_bar).click() 
        sleep(5) 
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().retail_catalog).click()
        sleep(5)       
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().design).click()    
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().add_design).click()
        sleep(5)        
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().design_name).send_keys(data.Logi_Data().design_name)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().design_inactive).click()
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().design_active).click()
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().save_design_page).click()
        assert self.driver.title == 'Logimax Technology | Admin'
        print("SUCCESS : Unable to proceed the requested process design_name: {a}". format(a=data.Logi_Data.design_name,))
      
    def test_edit_design(self,booting_function):
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().username_inputBox).send_keys(data.Logi_Data().username)
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().password_inputBox).send_keys(data.Logi_Data().password)
        sleep(4)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().signButton).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().side_bar).click() 
        sleep(5) 
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().retail_catalog).click()
        sleep(7)       
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().design).click() 
        sleep(5)       
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().edit_design).click()
        sleep(4)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().save_design_page).click()
        assert self.driver.title == 'Logimax Technology | Admin'
        print("SUCCESS : update successfully ")
      
        
    def test_delete_design(self,booting_function):
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().username_inputBox).send_keys(data.Logi_Data().username)
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().password_inputBox).send_keys(data.Logi_Data().password)
        sleep(4)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().signButton).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().side_bar).click() 
        sleep(5) 
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().retail_catalog).click()
        sleep(5)       
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().design).click() 
        sleep(5)       
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().delete_design).click()
        sleep(4)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().delete).click()    
        assert self.driver.title == 'Logimax Technology | Admin'
        print("SUCCESS : deteled successfully ")
      