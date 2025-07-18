import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.macros import Macros

keyboard = KMKKeyboard()
keyboard.modules = [Macros()]

keyboard.col_pins = (board.A0, board.A1, board.A2, board.A3)  # D0–D3
keyboard.row_pins = (board.D10, board.D9, board.D8, board.D6)  # D10, D9, D8, D6

keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [KC.A, KC.LSHIFT, KC.SPACE, KC.CAPS, KC.W, KC.TAB, KC.Q, KC.E, KC.S, KC.Z, KC.X, KC.C, KC.D, KC.F, KC.R, KC.G],

]

keyboard.go()
