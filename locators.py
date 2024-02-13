# File to store locators
# Classname should reflect either the page or the component it is related to

from selenium.webdriver.common.by import By

class AuthPageLocators:
    
    MAIN_LOGO = "xpath=//img[@id='logo']"
    LOGIN_FIELD = "xpath=//input[@name='username']"
    PASSWORD_FIELD = "xpath=//input[@name='password']"
    EYE_ICON = "xpath=//div[contains(@class, 'eye-icon-wrapper-web')]"
    LOGIN_BUTTON = "xpath=//button[@id='login-button']"
    RECOVER_ACCESS_LINK = "xpath=//a[@data-target='#reset-password-dialog']"
    CHANGE_LANGUAGE_LINK = "xpath=(//div[@class='secondary-links']/a)[1]"
    ABOUT_THE_BANK_LINK = "xpath=(//div[@class='secondary-links']/a)[2]"
    
    
    
    