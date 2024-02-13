from ..exceptions.base_exceptions import ElementNotVisible


class BasePage:
    
    def __init__(self, browser):
        self.browser = browser
        
    def element_to_be_visible(self, locator, state = 'visible', timeout = 30000):
        try:
            element = self.browser.locator(locator)
            return element.wait_for(state = state, timeout = timeout)
        except:
            raise ElementNotVisible(locator)
    
    def element_to_be_clickable(self):
        pass
        
    def click_on_element(self):
        pass
    
    def double_click_on_element(self):
        pass
    
    def press_key(self):
        pass
    
    def refresh_page(self):
        pass
    
    def take_screenshot(self):
        pass
    
    