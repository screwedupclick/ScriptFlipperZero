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

# Ouvrir un terminal (Ctrl + Alt + T sous Linux, Win + R puis "cmd" sous Windows)
keyboard.send(Keycode.CONTROL, Keycode.ALT, Keycode.T)  # Pour Linux
# keyboard.send(Keycode.GUI, Keycode.R)  # Pour Windows
# time.sleep(1)
# keyboard_layout.write("cmd")
# keyboard.send(Keycode.ENTER)

# Attendre que le terminal s'ouvre
time.sleep(1)

# Afficher un message éducatif
message = "Attention ! Votre session aurait pu être compromise. Verrouillez toujours votre ordinateur lorsque vous vous éloignez."
keyboard_layout.write(f"echo '{message}'")
keyboard.send(Keycode.ENTER)