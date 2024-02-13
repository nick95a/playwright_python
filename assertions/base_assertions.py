from playwright.sync_api import expect

def assert_text_content(element, expected_value):
    
    assert element.text_content() == expected_value, f"Value is not {expected_value}"
    
def check_element_is_visible(element):
    expect(element, f"Элемент {element} не отображается").to_be_visible()
    
def check_element_contains_text(element, expected_text):
    expect(element, "Элемент не содержит текст").to_contain_text(expected_text)
    
def check_input_has_value(element, expected_value):
    expect(element, "Input элемент не содержит значение").to_have_value(expected_value)
    
def check_website_has_url(element, expected_url):
    expect(element, "У веб-страницы другой url").to_have_url(expected_url)
    
