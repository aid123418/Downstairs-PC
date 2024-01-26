from pynput.mouse import Button, Controller
from pynput import keyboard
import time

# Set the target key combination to stop the autoclicker
stop_key = {keyboard.Key.ctrl, keyboard.KeyCode.from_char('o')}
current_keys = set()

# Function to simulate a click
def click():
    mouse = Controller()
    mouse.click(Button.left)

# Function to check key events
def on_press(key):
    if any([key in stop_key for stop_key in [keyboard.Key.ctrl, keyboard.KeyCode.from_char('o')]]):
        current_keys.add(key)
        if all([k in current_keys for k in stop_key]):
            # Exit the program if all stop keys are pressed
            return False

# Main game loop
with keyboard.Listener(on_press=on_press) as listener:
    while True:
        # Simulate a click
        click()

        # Add a delay to control the click rate (adjust as needed)
        time.sleep(5)
