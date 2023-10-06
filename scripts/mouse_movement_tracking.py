import csv
import time
from datetime import datetime
import pyautogui
from pynput import mouse

# Global variable to store mouse click state
mouse_click = None

# Mouse click callback for pynput listener
def on_click(x, y, button, pressed):
    global mouse_click
    if pressed:
        mouse_click = button.name

# Initialize CSV file and headers
def initialize(filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["timestamp", "x", "y", "mouse_click", "active_window_title"])

# Record mouse position, click, and active window title to CSV
def record_position(filename, timestamp, x, y, mouse_click, active_window_title):
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, x, y, mouse_click, active_window_title])

# Main loop to record data
def main_loop(record_length, interval=0.001):
    global mouse_click
    mouse_click = None  # Initialize mouse_click

    end_time = time.time() + record_length
    filename = "../output/mouse_data_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".csv"
    
    initialize(filename)
    
    # Start mouse listener in the background
    listener = mouse.Listener(on_click=on_click)
    listener.start()

    while time.time() < end_time:
        x, y = pyautogui.position()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        active_window_title = pyautogui.getActiveWindowTitle()
        
        record_position(filename, timestamp, x, y, mouse_click, active_window_title)
        
        mouse_click = None  # Reset mouse click state after recording
        time.sleep(interval)

    listener.stop()


if __name__ == "__main__":
    record_length = float(input("Enter the recording duration in seconds: "))
    main_loop(record_length)