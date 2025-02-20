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

# Ouvrir un éditeur de texte (Bloc-notes sous Windows)
keyboard.send(Keycode.GUI, Keycode.R)
time.sleep(1)
keyboard_layout.write("notepad")
keyboard.send(Keycode.ENTER)

# Attendre que l'éditeur de texte s'ouvre
time.sleep(1)

# Afficher un message de ransomware fictif
message = """ATTENTION !
Vos fichiers ont été chiffrés par un ransomware.
Ceci est une simulation éducative.
Pour éviter ce type d'attaque, verrouillez toujours votre session et ne cliquez pas sur des liens suspects.
"""
keyboard_layout.write(message)