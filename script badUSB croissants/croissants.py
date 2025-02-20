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

# Message à envoyer
message = "@DEVWEB2 je vous ramène des croissants cette semaine car j'ai oublié de verrouiller ma session <3"

# Envoi du message
keyboard_layout.write(message)

# Envoyer la touche Entrée pour soumettre le message
keyboard.send(Keycode.ENTER)