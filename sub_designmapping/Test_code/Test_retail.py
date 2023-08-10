
# app.py - The main executable file
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.options import Options
from time import sleep
from Test_locators import locators
from Test_data import data
import pytest


class Test_Logimax:
    @pytest.fixture
    

    def booting_function(self):
       self.driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
       self.driver.get(data.Logi_Data().url)
       self.driver.maximize_window()
       self.driver.implicitly_wait(5)
       
        
    def test_sub_design_mapping(self,booting_function):
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().username_inputBox).send_keys(data.Logi_Data().username)
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().password_inputBox).send_keys(data.Logi_Data().password)
        
        sleep(3)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().signButton).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().side_bar).click() 
        sleep(3) 
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().retail_catalog).click()
        sleep(5)      
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().sub_design_mapping).click()    
        sleep(8)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().select_product_maping).click()
        sleep(6)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().select_product_mapping_list).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().select_design_mapping).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().select_design_mapping_list).click()
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().select_sub_design).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().search_sub_design_list).click()
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().update1).click() 
        assert self.driver.title == 'Logimax Technology | Admin'
        print("SUCCESS : The sub design mapping list added successfully ")
        
        
        
    def test_search_subdesign_mapping(self,booting_function):
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().username_inputBox).send_keys(data.Logi_Data().username)
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().password_inputBox).send_keys(data.Logi_Data().password)
        
        sleep(3)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().signButton).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().side_bar).click() 
        sleep(3) 
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().retail_catalog).click()
        sleep(5)      
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().sub_design_mapping).click()    
        sleep(8)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().search_product_maping).click()
        sleep(6)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().search_mapping_list).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().search_design_mapping).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().search_mapping_area).click()
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().search_sub_design).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().search_sub_design_list).click()
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().search_button).click() 
        assert self.driver.title == 'Logimax Technology | Admin'
        print("SUCCESS : Filter Detail Run Successfully")    
    
    
    
    def test_delete_subdesign_mapping(self,booting_function):
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().username_inputBox).send_keys(data.Logi_Data().username)
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().password_inputBox).send_keys(data.Logi_Data().password)
        
        sleep(3)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().signButton).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().side_bar).click() 
        sleep(3) 
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().retail_catalog).click()
        sleep(5)      
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().sub_design_mapping).click()    
        sleep(8)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().delete).click()
        sleep(6)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().delete_sub_design).click()
        assert self.driver.title == 'Logimax Technology | Admin'
        print("SUCCESS : Deleted mapping Successfully") 