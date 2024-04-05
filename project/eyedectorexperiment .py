import tobii_research as tr
import pyautogui

# Initialize the eye tracker
eyetracker = tr.find_all_eyetrackers()[0]

# Connect to the eye tracker
eyetracker.connect()

# Function to move the mouse based on gaze data
def move_mouse(gaze_data):
    x = gaze_data['left_gaze_point_on_display_area'][0]
    y = gaze_data['left_gaze_point_on_display_area'][1]
    
    screen_width, screen_height = pyautogui.size()
    target_x = int(screen_width * x)
    target_y = int(screen_height * y)
    
    pyautogui.moveTo(target_x, target_y)

try:
    # Subscribe to gaze data
    eyetracker.subscribe_to(tr.EYETRACKER_GAZE_DATA, move_mouse)

    # Keep the program running
    input("Press Enter to exit...")
finally:
    # Unsubscribe and disconnect when done
    eyetracker.unsubscribe_from(tr.EYETRACKER_GAZE_DATA, move_mouse)
    eyetracker.disconnect()
