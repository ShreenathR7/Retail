
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
       

    def test_sub_design(self,booting_function):
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().username_inputBox).send_keys(data.Logi_Data().username)
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().password_inputBox).send_keys(data.Logi_Data().password)
        sleep(3)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().signButton).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().side_bar).click() 
        sleep(3)    
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().retail_catalog).click()
        sleep(5)  
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().sub_design).click()    
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().add_sub_design).click()
        sleep(8)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().sub_design_name).send_keys(data.Logi_Data().sub_design)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().save_subdesign_page).click()
        assert self.driver.title == 'Logimax Technology | Admin'
        print("SUCCESS : The design list added successfully sub_design_name: {a}". format(a=data.Logi_Data.sub_design))
           
    def test_double_entry_sub_design(self,booting_function):
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().username_inputBox).send_keys(data.Logi_Data().username)
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().password_inputBox).send_keys(data.Logi_Data().password)
        sleep(3)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().signButton).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().side_bar).click() 
        sleep(3)    
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().retail_catalog).click()
        sleep(5)  
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().sub_design).click()    
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().add_sub_design).click()
        sleep(8)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().sub_design_name).send_keys(data.Logi_Data().sub_design)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().save_subdesign_page).click()
        assert self.driver.title == 'Logimax Technology | Admin'
        print("SUCCESS : Unable to proceed the requested process  sub_design_name: {a}". format(a=data.Logi_Data.sub_design))        
        
    def test_edit_sub_design(self,booting_function):
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().username_inputBox).send_keys(data.Logi_Data().username)
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().password_inputBox).send_keys(data.Logi_Data().password)
        sleep(3)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().signButton).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().side_bar).click() 
        sleep(3)    
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().retail_catalog).click()
        sleep(5)  
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().sub_design).click()    
        sleep(6)      
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().edit).click()
        sleep(5)   
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().sub_design_name).clear()
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().sub_design_name).send_keys(data.Logi_Data().design_name)
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().save_subdesign_page).click()
        assert self.driver.title == 'Logimax Technology | Admin'
        print("SUCCESS : Updated sub design name successfully")        
        
        
        
    
    def test_delete_sub_design(self,booting_function):
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().username_inputBox).send_keys(data.Logi_Data().username)
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().password_inputBox).send_keys(data.Logi_Data().password)
        sleep(3)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().signButton).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().side_bar).click() 
        sleep(3)    
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().retail_catalog).click()  
        sleep(5)  
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().sub_design).click()    
        sleep(5)    
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().delete).click()  
        sleep(5)    
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().delete_sub_design).click()  
        assert self.driver.title == 'Logimax Technology | Admin'
        print("SUCCESS :Delated sub design name successfully")        
        