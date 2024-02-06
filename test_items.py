from selenium.webdriver.common.by import By
from time import sleep

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


class TestLanguage:

    def test_add_item_button(self, browser):
        browser.get(link)
        sleep(3)
        add_to_cart_btn = browser.find_elements(By.CSS_SELECTOR, 'button.btn-add-to-basket')

        assert add_to_cart_btn, f'No such button on the page {link}'
