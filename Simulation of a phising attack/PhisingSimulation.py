import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

# Initialisation du clavier
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)

# Temps d'attente pour permettre à la machine de reconnaître le clavier
time.sleep(2)

# Ouvrir un navigateur (Win + R, puis "chrome" ou "firefox")
keyboard.send(Keycode.GUI, Keycode.R)
time.sleep(1)
keyboard_layout.write("chrome")  # Ou "firefox" selon le navigateur
keyboard.send(Keycode.ENTER)

# Attendre que le navigateur s'ouvre
time.sleep(2)

# Accéder à une URL éducative (par exemple, une page de sensibilisation)
keyboard_layout.write("https://www.cybermalveillance.gouv.fr")
keyboard.send(Keycode.ENTER)

# Afficher un message dans la console
time.sleep(2)
keyboard.send(Keycode.CONTROL, Keycode.SHIFT, Keycode.J)  # Ouvrir la console du navigateur
time.sleep(1)
keyboard_layout.write("console.log('Votre navigateur aurait pu être redirigé vers un site malveillant. Soyez vigilant !');")
keyboard.send(Keycode.ENTER)