import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

# Initialisation du clavier
keyboard = Keyboard(usb_hid.devices)

# Temps d'attente pour permettre à la machine de reconnaître le clavier
time.sleep(2)

# Verrouiller l'écran (Win + L sous Windows, Ctrl + Alt + L sous Linux)
keyboard.send(Keycode.GUI, Keycode.L)  # Pour Windows
# keyboard.send(Keycode.CONTROL, Keycode.ALT, Keycode.L)  # Pour Linux