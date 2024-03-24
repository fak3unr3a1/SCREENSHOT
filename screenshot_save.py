# screenshot_save.py
from datetime import datetime

def save_screenshot(image):
    # Generate a timestamp for the filename
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # Save the screenshot with the timestamp as the filename
    filename = f"screenshot_{timestamp}.png"
    image.save(filename)

    return filename
