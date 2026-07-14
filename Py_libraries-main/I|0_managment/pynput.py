import threading
import time
from pynput.mouse import Button, Controller as Mouse, Listener as MouseListener
from pynput.keyboard import Key, Controller as Keyboard, Listener as KeyboardListener

# ===== MOUSE CONTROL =====
mouse = Mouse()
print('Current pointer position:', mouse.position)

mouse.position = (10, 20)
print('New position:', mouse.position)

mouse.move(5, -5)
mouse.press(Button.left)
mouse.release(Button.left)
mouse.click(Button.left, 2)  # double click
mouse.scroll(0, 2)  # scroll down 2 steps

# ===== MOUSE LISTENER =====
def on_move(x, y):
    print(f'Moved to ({x}, {y})')

def on_click(x, y, button, pressed):
    print(f'{"Pressed" if pressed else "Released"} {button} at ({x}, {y})')
    if not pressed:
        # Stop listener on release
        return False

def on_scroll(x, y, dx, dy):
    print(f'Scrolled {"down" if dy < 0 else "up"} at ({x}, {y})')

mouse_listener = MouseListener(on_move=on_move, on_click=on_click, on_scroll=on_scroll)

# ===== KEYBOARD CONTROL =====
keyboard = Keyboard()
keyboard.press(Key.space)
keyboard.release(Key.space)

keyboard.press('a')
keyboard.release('a')
# keyboard.tap('a')  # закомментил, чтобы не дублировать

with keyboard.pressed(Key.shift):
    keyboard.press('a')
    keyboard.release('a')

keyboard.type('Hello World')

# ===== KEYBOARD LISTENER =====
def on_press(key):
    try:
        print(f'Alphanumeric key {key.char} pressed')
    except AttributeError:
        print(f'Special key {key} pressed')

def on_release(key):
    print(f'{key} released')
    if key == Key.esc:
        return False  # stop listener

keyboard_listener = KeyboardListener(on_press=on_press, on_release=on_release)

# ===== RUN LISTENERS IN BACKGROUND =====
mouse_listener.start()
keyboard_listener.start()

# Keep main thread alive
try:
    while mouse_listener.is_alive() and keyboard_listener.is_alive():
        time.sleep(0.1)
except KeyboardInterrupt:
    mouse_listener.stop()
    keyboard_listener.stop()
