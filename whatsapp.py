'''
sudo apt-get install chromium-chromedriver
pip install selenium
'''
import os
from utils import Whatsapp

os_path = os.path.dirname(os.path.realpath(__file__))
whatsapp = Whatsapp(os_path+'/chromedata')

text = "Hey, this message was sent using Selenium"
# whatsapp.send_message_to_chat(chat_name='Test', message=text) # TESTED
# whatsapp.add_to_group(group_name='Test', contact_name='پوریا') # TESTED
# whatsapp.send_message_to_chat(chat_name='Test', message='Hi, you were just added to this group using selenium.') # TESTED
whatsapp.find_all_groups(search='dovinance')
whatsapp.quit_driver()