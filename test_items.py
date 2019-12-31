from selenium import webdriver
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_button(browser):
        browser.get(link)
        button1 = str(browser.find_element_by_class_name('btn-add-to-basket').get_attribute("class"))
        assert button1=="btn btn-lg btn-primary btn-add-to-basket", "Кнопка не найдена"


                
