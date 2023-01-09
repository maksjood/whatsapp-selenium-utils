'''
sudo apt-get install chromium-chromedriver
pip install selenium
'''
import os
from utils import Whatsapp, OSType

os_path = os.path.dirname(os.path.realpath(__file__))
whatsapp = Whatsapp(os_path+'/chromedata', os_type=OSType.LINUX)

# text = '''سلام 😎.

# چه میکنه جواد'''
# file = os.path.abspath(os_path+'/wapptest.png')
# whatsapp.send_message_to_chat(chat_name='Test', message=text, image_path=file)
# whatsapp.remove_from_group(group_name='Test', contact_name='پوریا', contact_phone_number='+989362190659')
# whatsapp.add_to_group(group_name='Test', contact_name='پوریا', contact_phone_number='+989362190659')
whatsapp.make_admin_to_group(group_name='Test', contact_phone_number='+989362190659')
# text = 'Pourya been just removed, added and made admin by dovinance cool whatsapp bot.'
# whatsapp.send_message_to_chat(chat_name='Test', message=text)
# names = whatsapp.find_all_chats(search='dovinance')
whatsapp.quit_driver()