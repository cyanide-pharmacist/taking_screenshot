import pyautogui
import datetime
import os
import time
import winsound
from winotify import Notification

folder_path = r"C:\Users\Cyanide\Desktop\Screenshot"
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

interval = 1800  # 30 minutes (changed 30 to 1800 seconds)

# <-- Add your custom sound file path here -->
custom_sound_path = r"C:\Users\Cyanide\Desktop\Screenshot\tone.wav"

while True:
    # Toast Notification using winotify (auto-close)
    notifier = Notification(
        app_id="Screenshot App",
        title="⚡ Hold On!",
        msg="📸 Screenshot in 3 seconds...",
        duration="short"
    )
    notifier.show()

    # Play your custom sound (waits until sound finishes)
    winsound.PlaySound(custom_sound_path, winsound.SND_FILENAME)

    # Or, if you want it async (non-blocking), use:
    # winsound.PlaySound(custom_sound_path, winsound.SND_FILENAME | winsound.SND_ASYNC)
    # And add time.sleep(duration_of_sound_in_seconds)

    timestamp = datetime.datetime.now().strftime("%A_%Y-%m-%d_%H-%M-%S")
    file_name = f'{timestamp}.png'
    file_path = os.path.join(folder_path, file_name)

    screenshot = pyautogui.screenshot()
    screenshot.save(file_path)

    print(f"✅ Screenshot saved to: {file_path}")
    print(f"⏱ Waiting {interval // 60} minutes...\n")

    time.sleep(interval)
