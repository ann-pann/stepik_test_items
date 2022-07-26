from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_to_basket_button_exists(browser):
    browser.get(link)
    button = browser.find_elements(By.XPATH, "//*[contains(@class,'btn-add-to-basket')]")
    assert button, 'Button is not exist'
