import time
from typing import Iterable, Tuple
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium import webdriver
from selenium.common.exceptions import TimeoutException

class Locators:
    chat_search = (By.XPATH, '//div[@data-testid="chat-list-search"]')
    chat_search_close_button = (By.XPATH, '//span[@data-testid="x-alt"]')
    input_box = (By.XPATH, '//p[@class="selectable-text copyable-text"]')
    chat_header = (By.XPATH, '//header[@data-testid="conversation-header"]')
    add_user = (By.XPATH, '//span[@data-testid="add-user"]')
    check_mark = (By.XPATH, '//span[@data-testid="checkmark-medium"]')
    confirm = (By.XPATH, '//div[@data-testid="popup-controls-ok"]')
    search_results_CHATS_divider = (By.XPATH, '//div[@class="YGe90 MCwxg"][text() = "Chats"]')
    search_results_MESSAGES_divider = (By.XPATH, '//div[@class="YGe90 MCwxg"][text() = "Messages"]')
    search_results_CONTACTS_divider = (By.XPATH, '//div[@class="YGe90 MCwxg"][text() = "Contacts"]')
    chat_label = (By.XPATH, '//div[@class="zoWT4"]')

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

    def _find_elements(self, locator, timeout=999):
        WebDriverWait(self.driver, timeout=timeout).until(
            lambda driver: driver.find_element(*locator))
        time.sleep(.5)
        return self.driver.find_elements(*locator)

    def _search_for_chat(self, search: str, timeout:int=999):
        input_box_search = self._find_elements(locator=Locators.chat_search, timeout=timeout)[0]
        input_box_search.click()
        input_box_search.clear()
        input_box_search.send_keys(search)

    def quit_driver(self):
        self.driver.quit()

    def _go_to_chat(self, chat_name, chat_phone_number:str = None):
        '''for the search to work, `chat_phone_number` must be part of the full phone number (+989...)'''
        self._search_for_chat(search=chat_phone_number or chat_name)
        chat = self._find_elements(locator=Locators.chat(chat_name=chat_name))[0]
        chat.click()
        time.sleep(.5)
        return chat

    def send_message_to_chat(self, chat_name, message, chat_phone_number: str = None):
        self._go_to_chat(chat_name=chat_name, chat_phone_number=chat_phone_number)
        input_box = self._find_elements(locator=Locators.input_box)[0]
        input_box.send_keys(message + Keys.ENTER)
        time.sleep(2)

    def add_to_group(self, group_name, contact_name, contact_phone_number: str = None):
        self._go_to_chat(chat_name=group_name)
        self._find_elements(locator=Locators.chat_header)[0].click()
        self._find_elements(locator=Locators.add_user)[0].click()
        search_box = self.driver.switch_to.active_element
        search_box.send_keys(contact_phone_number or contact_name)
        self._find_elements(locator=Locators.chat(chat_name=contact_name))[0].click()
        time.sleep(.5)
        self._find_elements(locator=Locators.check_mark)[0].click()
        time.sleep(.5)
        self._find_elements(locator=Locators.confirm)[0].click()
        time.sleep(0.5)

    def find_all_chats(self, search: str):
        self._search_for_chat(search=search)
        try:
            chats_divider = self._find_elements(locator=Locators.search_results_CHATS_divider)[0]
        except TimeoutException:
            raise Exception(f'Chat with name "{search}" was not found.')
        names = set()
        prev_butt_elem = None
        while True:
            new_elems = self._find_elements(locator=Locators.chat_label)
            names.update({elem.text for elem in new_elems if search.lower() in elem.text.lower()})
            butt_elem = new_elems[0]
            for elem in new_elems:
                if elem.location['y'] > butt_elem.location['y']:
                    butt_elem = elem
            if prev_butt_elem and prev_butt_elem==butt_elem:
                break
            prev_butt_elem = butt_elem
            try:
                self._find_elements(locator=Locators.search_results_CONTACTS_divider, timeout=.1)
                break
            except TimeoutException:
                try:
                    self._find_elements(locator=Locators.search_results_MESSAGES_divider, timeout=.1)
                    break
                except TimeoutException:
                    webdriver.ActionChains(self.driver).scroll_to_element(butt_elem).perform()
        return list(names)