import time
from typing import Iterable, Tuple
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium import webdriver

class Locators:
    chat_search = (By.XPATH, '//div[@data-testid="chat-list-search"]')
    chat_search_close_button = (By.XPATH, '//span[@data-testid="x-alt"]')
    input_box = (By.XPATH, '//p[@class="selectable-text copyable-text"]')
    chat_header = (By.XPATH, '//header[@data-testid="conversation-header"]')
    add_user = (By.XPATH, '//span[@data-testid="add-user"]')
    check_mark = (By.XPATH, '//span[@data-testid="checkmark-medium"]')
    confirm = (By.XPATH, '//div[@data-testid="popup-controls-ok"]')
    search_
    def chat(chat_name: str):
        return (By.XPATH, f"//span[@title='{chat_name}']")

class Whatsapp:
    def __init__(self, user_data_path: str):
        options = webdriver.ChromeOptions()
        options.add_argument(f"--user-data-dir={user_data_path}")
        # options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)
        driver.get("https://web.whatsapp.com")
        self.driver: WebDriver = driver

    def _find_element(self, locator, timeout=5):
        WebDriverWait(self.driver, timeout=timeout).until(
            lambda driver: self.driver.find_element(*locator))
        time.sleep(.5)
        return self.driver.find_element(*locator)
    
    def _search_for_chat(self, search: str, timeout:int=20):
        input_box_search = self._find_element(locator=Locators.chat_search, timeout=timeout)
        input_box_search.click()
        input_box_search.clear()
        input_box_search.send_keys(search)

    def quit_driver(self):
        self.driver.quit()
    

    def go_to_chat(self, chat_name, chat_phone_number:str = None):
        '''for the search to work, `chat_phone_number` must be part of the full phone number (+989...)'''
        # input_box_search = self._find_element(locator=Locators.chat_search, timeout=20)
        # input_box_search.click()
        # input_box_search.clear()
        # input_box_search.send_keys(chat_phone_number or chat_name)
        self._search_for_chat(search=chat_phone_number or chat_name)
        chat = self.find_element(locator=Locators.chat(chat_name=chat_name))
        chat.click()
        time.sleep(.5)
        return chat

    def send_message_to_chat(self, chat_name, message, chat_phone_number):
        self.go_to_chat(chat_name=chat_name, chat_phone_number=chat_phone_number)
        input_box = self.find_element(locator=Locators.input_box)
        input_box.send_keys(message + Keys.ENTER)
        time.sleep(2)

    def add_to_group(self, group_name, contact_name, contact_phone_number: str):
        self.go_to_chat(chat_name=group_name)
        self.find_element(locator=Locators.chat_header).click()
        self.find_element(locator=Locators.add_user).click()
        search_box = self.driver.switch_to.active_element
        search_box.send_keys(contact_phone_number)
        self.find_element(locator=Locators.chat(chat_name=contact_name)).click()
        time.sleep(.5)
        self.find_element(locator=Locators.check_mark).click()
        time.sleep(.5)
        self.find_element(locator=Locators.confirm).click()
        time.sleep(0.5)

    def find_all_groups(self, search: str):
        pass