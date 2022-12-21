The core of this projects is the `utils.py`. `whatsapp.py` is an example script that employs `utils.py`.
You're gonna need to run `apt-get install chromium-chromedriver` and `apt install copyq` before hand.

As you know, WhatsApp needs logging in with QRCode scanning. If you don't want to do it everytime you use this project, provide a chromedata directory which is compatible with selenium chromedriver. It is best that you priovide an empty path when instanciating a `utils.Whatsapp` object, loging using your phone and use the same path for later use.