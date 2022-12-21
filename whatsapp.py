'''
sudo apt-get install chromium-chromedriver
pip install selenium
'''
import os
from utils import Whatsapp, OSType

os_path = os.path.dirname(os.path.realpath(__file__))
whatsapp = Whatsapp(os_path+'/chromedata', os_type=OSType.LINUX)

text = '''سلام 😎.

چه میکنه جواد'''
file = os.path.abspath(os_path+'/wapptest.png')
whatsapp.send_message_to_chat(chat_name='Test', message=text, image_path=file) # TESTED
# whatsapp.add_to_group(group_name='Test', contact_name='پوریا') # TESTED
# names = whatsapp.find_all_chats(search='dovinance')
whatsapp.quit_driver()