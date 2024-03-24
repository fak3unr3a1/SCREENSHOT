# main_script.py
from screenshot_capture import capture_screenshot
from screenshot_save import save_screenshot

def main():
    # Capture the screenshot
    screenshot_image = capture_screenshot()

    # Save the screenshot
    screenshot_filename = save_screenshot(screenshot_image)

    print(f"Screenshot saved as: {screenshot_filename}")

if __name__ == "__main__":
    main()
