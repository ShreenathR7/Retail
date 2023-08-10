
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
        

    def test_design_mapping(self,booting_function):
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().username_inputBox).send_keys(data.Logi_Data().username)
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().password_inputBox).send_keys(data.Logi_Data().password)
       
        sleep(3)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().signButton).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().side_bar).click() 
        sleep(4)  
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().retail_catalog).click()
        sleep(5)    
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().design_mapping).click()    
        sleep(4)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().select_product).click()
        sleep(5)             
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().select_product_list).click()
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().select_design).click()
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().select_design_list).click()
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().update).click()
        assert self.driver.title == 'Logimax Technology | Admin'
        print("SUCCESS : The design mapping list added successfully ")
        
        
    def test_search_design_mapping(self,booting_function):
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().username_inputBox).send_keys(data.Logi_Data().username)
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().password_inputBox).send_keys(data.Logi_Data().password)
       
        sleep(3)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().signButton).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().side_bar).click() 
        sleep(4)  
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().retail_catalog).click()
        sleep(5)    
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().design_mapping).click()    
        sleep(4)  
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().search_product).click() 
        sleep(4)  
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().search_product_list).click()
        sleep(5)    
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().search_design).click()    
        sleep(4)  
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().search_design_list).click() 
        sleep(6)  
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().search_button).click()
        assert self.driver.title == 'Logimax Technology | Admin'
        print("SUCCESS : filter details run successfully ")
    
    def  test_delete_design_mapping(self,booting_function):
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().username_inputBox).send_keys(data.Logi_Data().username)
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().password_inputBox).send_keys(data.Logi_Data().password)
       
        sleep(3)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().signButton).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().side_bar).click() 
        sleep(4)  
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().retail_catalog).click()
        sleep(5)    
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().design_mapping).click()    
        sleep(4)  
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().delete_mapping).click() 
        sleep(4)  
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().delete_mapping_page).click() 
        assert self.driver.title == 'Logimax Technology | Admin'
        print("SUCCESS : Delete mapping  ")
        
    