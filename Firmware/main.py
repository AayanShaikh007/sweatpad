import board
import busio

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.macros import Macros

from kmk.extensions.display import Display, TextEntry
from kmk.extensions.LED import LED, AnimationModes
from kmk.extensions.display.ssd1306 import SSD1306


col_0 = board.GP1
col_1 = board.GP2
col_2 = board.GP3
col_3 = board.GP4


row_0 = board.GP11
row_1 = board.GP10
row_2 = board.GP9
row_3 = board.GP7

led_pin = board.GP8

oled_bus = busio.I2C(board.GP_SCL, board.GP_SDA)

oled_driver = SSD1306(i2c=oled_bus, device_address=0x3C);

display = Display(
    display=oled_driver,
    width=128,
    height=64,   # isnt this supposed to be 32 bit
    dim_time=10,
    dim_target=0.2,
    off_time=1200,
    brightness=0.8
);

keyboard = KMKKeyboard()
keyboard.diode_orientation = DiodeOrientation.COL2ROW # the stripe (+) points towards the row 

keyboard.col_pins = (col_0, col_1, col_2, col_3);
keyboard.row_pins = (row_0, row_1, row_2, row_3);

keyboard.keymap = [
    [KC.Q,      KC.W,     KC.E,      KC.R  ],  # Row 0
    [KC.A,      KC.S,     KC.D,      KC.F  ],  
    [KC.LSHIFT, KC.LTAB,  KC.LCAPS,  KC.SPACE  ],  #THIS NEEDS FIXING -- the actual keys are arranged differently
    [KC.Z,      KC.X,     KC.C,      KC.V],  
]

if __name__ == '__main__':
    keyboard.go()