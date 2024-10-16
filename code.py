import usb_hid
import time
import board
from adafruit_hid.keyboard import Keyboard
from keycode_win_sw import Keycode
from keyboard_layout_win_sw import KeyboardLayout

# Set up a keyboard device.
kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayout(kbd)

time.sleep(1)
kbd.send(Keycode.WINDOWS, Keycode.R)
time.sleep(1)
layout.write('cmd\n')
time.sleep(1)
layout.write('@echo "HELLO WORLD"\n')
kbd.send(Keycode.SHIFT, Keycode.ENTER)
layout.write('exit\n')
