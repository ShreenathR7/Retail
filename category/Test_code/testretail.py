
# app.py - The main executable file
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import Select
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
    
         
    def test_category_entry(self,booting_function):   
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().username_inputBox).send_keys(data.Logi_Data().username)
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().password_inputBox).send_keys(data.Logi_Data().password)
        sleep(3)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().signButton).click()
        sleep(8)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().side_bar).click() 
        sleep(5) 
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().retail_catalog).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().category_module2).click()
        sleep(8)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().add_category).click()
        sleep(5)        
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().active_no).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().active_Yes).click()
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().category_name).send_keys(data.Logi_Data().categoryname)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().HSN_code).send_keys(data.Logi_Data().HSN_no)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().short_no).send_keys(data.Logi_Data().Short_code_no)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().bullion).click()
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().stone).click()
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().alloy).click()
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().ornament).click()
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().multi_level_yes).click()
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().multi_level_no).click()
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().list_metal).click()
        sleep(3)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().select_metal).click()
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().select_tax).click()
        sleep(3)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().select_tax_group).click()
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().purity).click()
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().select_purity).click()
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().purity).click()
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().select_purity1).click()
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().purity).click()
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().select_purity2).click()
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().remove_purity).click()       
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().category_save).click()
        assert self.driver.title == 'Logimax Technology | Admin'
        print("SUCCESS : The category list added successfully category_name: {a},HSN_code: {b} & Short_no: {c}". format(a=data.Logi_Data.categoryname, b=data.Logi_Data.HSN_no, c=data.Logi_Data.Short_code_no))
   
       
    def test_double_category_entry(self,booting_function):   
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().username_inputBox).send_keys(data.Logi_Data().username)
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().password_inputBox).send_keys(data.Logi_Data().password)
        sleep(3)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().signButton).click()
        sleep(8)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().side_bar).click() 
        sleep(5) 
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().retail_catalog).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().category_module2).click()
        sleep(8)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().add_category).click()
        sleep(5)        
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().active_no).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().active_Yes).click()
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().category_name).send_keys(data.Logi_Data().categoryname)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().HSN_code).send_keys(data.Logi_Data().HSN_no)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().short_no).send_keys(data.Logi_Data().Short_code_no)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().bullion).click()
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().stone).click()
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().alloy).click()
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().ornament).click()
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().multi_level_yes).click()
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().multi_level_no).click()
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().list_metal).click()
        sleep(3)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().select_metal).click()
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().select_tax).click()
        sleep(3)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().select_tax_group).click()
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().purity).click()
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().select_purity).click()
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().purity).click()
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().select_purity1).click()
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().purity).click()
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().select_purity2).click()
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().remove_purity).click()       
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().category_save).click()
        assert self.driver.title == 'Logimax Technology | Admin'
        print("POP message : Unable to proceed the requested process..category_name: {a},HSN_code: {b} & Short_no: {c}". format(a=data.Logi_Data.categoryname, b=data.Logi_Data.HSN_no, c=data.Logi_Data.Short_code_no))
      
        
    def test_edit_category_entry(self,booting_function):   
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().username_inputBox).send_keys(data.Logi_Data().username)
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().password_inputBox).send_keys(data.Logi_Data().password)
        sleep(3)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().signButton).click()
        sleep(8)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().side_bar).click() 
        sleep(5) 
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().retail_catalog).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().category_module2).click()
        sleep(8)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().edit_category).click()
        sleep(5) 
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().edit_HSN_code).clear()
        sleep(5) 
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().edit_HSN_code).send_keys(data.Logi_Data().Hsn_code)
        sleep(5) 
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().update_category).click()
        assert self.driver.title == 'Logimax Technology | Admin'
        print("SUCCESS :Updated successfully ")
        
        
    def test_delete_category_entry(self,booting_function):   
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().username_inputBox).send_keys(data.Logi_Data().username)
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().password_inputBox).send_keys(data.Logi_Data().password)
        sleep(3)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().signButton).click()
        sleep(8)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().side_bar).click() 
        sleep(5) 
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().retail_catalog).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().category_module2).click()
        sleep(8)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().delete_category).click()    
        sleep(8)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().delete).click()    
        assert self.driver.title == 'Logimax Technology | Admin'
        print("SUCCESS :deleted successfully")
    
    
            
        
        