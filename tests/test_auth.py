# Contains smoke tests for the auth page

import pytest
import playwright

from playwright.sync_api import Playwright, sync_playwright, expect, Page
from expected_values import AuthExpectedValues
from ..pages.auth_page import AuthPage
from ..input_data import *
from ..locators import *
from ..expected_values import *

 
class TestAuthPage:
    
    @pytest.mark.skip
    @pytest.mark.smoke
    @pytest.mark.login
    @pytest.mark.ui
    def test_auth_page_url(self, auth_fixture):
        """Проверка наличия визуальных элементов на странице авторизации"""
        
        auth_page = AuthPage(auth_fixture).browser
        current_url = auth_page.url()
        
        assert current_url.find(URI.MAIN_HOST) != -1, "Текущий URL отличается от ожидаемого"
    
    @pytest.mark.skip
    @pytest.mark.smoke
    @pytest.mark.login
    @pytest.mark.ui
    def test_auth_page_presence_of_visual_elements(self, auth_fixture):
        """Проверка наличия визуальных элементов на странице авторизации"""
        
        auth_page = AuthPage(auth_fixture)
        auth_page.locator(AuthPageLocators.MAIN_LOGO)
        auth_page.locator(AuthPageLocators.LOGIN_FIELD)
        auth_page.locator(AuthPageLocators.PASSWORD_FIELD)
        auth_page.locator(AuthPageLocators.EYE_ICON)
        auth_page.locator(AuthPageLocators.LOGIN_BUTTON)
        auth_page.locator(AuthPageLocators.RECOVER_ACCESS_LINK)
        auth_page.locator(AuthPageLocators.ABOUT_THE_BANK_LINK)
    
    @pytest.mark.skip
    @pytest.mark.smoke
    @pytest.mark.login
    @pytest.mark.ui
    @pytest.mark.positive 
    def test_auth_page_login_placeholder(self, auth_fixture):
        
        """Проверка заполнения значением по умолчанию поля логина"""
        
        auth_page = AuthPage(auth_fixture).browser
        login_field = auth_page.locator(AuthPageLocators.LOGIN_FIELD)
        login_field.click()
        login_field.clear()
        login_placeholder = login_field.get_attribute("placeholder")
        assert login_placeholder == AuthExpectedValues.LOGIN_PLACEHOLDER

    @pytest.mark.skip
    @pytest.mark.smoke
    @pytest.mark.login
    @pytest.mark.ui
    @pytest.mark.positive 
    def test_auth_page_password_placeholder(self, auth_fixture):
        
        """Проверка заполнения значением по умолчанию поля пароля"""
        
        auth_page = AuthPage(auth_fixture).browser
        password_field = auth_page.locator(AuthPageLocators.PASSWORD_FIELD)
        password_field.click()
        password_field.clear()
        login_placeholder = password_field.get_attribute("placeholder")
        assert login_placeholder == AuthExpectedValues.PASSWORD_PLACEHOLDER, "Placeholder does not match"

    @pytest.mark.skip
    @pytest.mark.smoke
    @pytest.mark.login
    @pytest.mark.ui
    @pytest.mark.positive 
    def test_auth_page_password_hider_one(self, auth_fixture):
        
        """Проверка того, что данные пароля скрыты по умолчанию при загрузке страницы"""
        
        auth_page = AuthPage(auth_fixture).browser
        eye_button = auth_page.locator(AuthPageLocators.EYE_ICON)
        eye_button_default_class = eye_button.get_attribute("className")
        assert eye_button_default_class == AuthExpectedValues.EYE_ICON_DEFAULT_CLASS, "Eye icon off by default"
    
    @pytest.mark.skip
    @pytest.mark.smoke
    @pytest.mark.login
    @pytest.mark.ui
    @pytest.mark.positive 
    def test_auth_page_enter_button_default_text(self, auth_fixture):
        
        """Проверка того, что данные пароля скрыты по умолчанию при загрузке страницы"""
        
        auth_page = AuthPage(auth_fixture).browser
        login_button = auth_page.get_by_text("Войти")
        login_button_placeholder = login_button.text_content()
        assert login_button_placeholder == AuthExpectedValues.LOGIN_BUTTON_PLACEHOLDER, "Enter button default text is wrong"
    
    @pytest.mark.skip
    @pytest.mark.smoke
    @pytest.mark.login
    @pytest.mark.ui
    @pytest.mark.positive 
    def test_auth_page_recover_button_default_text(self, auth_fixture):
        
        """Проверка того, что кнопка восстановить видима и имеет ожидаемый текст"""
        
        auth_page = AuthPage(auth_fixture).browser
        expect(auth_page.locator(AuthPageLocators.RECOVER_ACCESS_LINK), "Recover button is visible").to_be_visible()
        recover_access_link = auth_page.wait_for_selector(AuthPageLocators.RECOVER_ACCESS_LINK)
        recover_access_link_text = recover_access_link.text_content()
        recover_access_link_text = recover_access_link_text.replace("\n", "")
        recover_access_link_text = recover_access_link_text.lstrip()
        recover_access_link_text = recover_access_link_text.rstrip()
        assert recover_access_link_text == AuthExpectedValues.RECOVER_LINK_PLACEHOLDER
        
        
        
        
    
        

        
