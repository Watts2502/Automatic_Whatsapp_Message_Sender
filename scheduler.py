import pyautogui
import webbrowser
import time
import datetime
import tkinter as tk
from tkinter import messagebox

def show_warning_box():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    messagebox.showinfo("Automation Notice", "WhatsApp automation will start in 30 seconds. Please get ready!")
    root.destroy()

def log_run(status):
    log_file = "<Insert path to your log file>"
    today = datetime.date.today().isoformat()
    with open(log_file, "a") as f:
        f.write(f"{today} - {status}\n")

def send_to_group(group_name, message):
    print(f"Sending to: {group_name}")
    
    # Click the search bar (adjust x, y as per your screen)
    pyautogui.click(x=135, y=240)
    time.sleep(0.8)
    
    pyautogui.write(group_name, interval=0.03)
    time.sleep(1.2)
    pyautogui.press('enter')
    time.sleep(0.8)

    pyautogui.write(message, interval=0.03)
    pyautogui.press('enter')
    print(f"Message sent to {group_name}")
    time.sleep(1.2)

# === Configuration ===
groups = ["Insert your group names/contact numbers here"]

message = "Insert your message here"
today = datetime.date.today()

# === Date checks (Change as per your requirement) ===
if today.weekday() == 6:  # 6 = Sunday
    print("It's Sunday. Skipping.")
    log_run("Skipped - Sunday")
    exit()

if today > datetime.date(2025, 8, 13):
    print("Schedule ended. Skipping.")
    log_run("Skipped - Schedule Ended")
    exit()

# === Display warning box for user to be prepared for automation ===
show_warning_box()
print("Waiting 1 minute before starting...")
time.sleep(30)

# === Open WhatsApp Web and send ===
print("Opening WhatsApp Web...")
webbrowser.open("https://web.whatsapp.com/")
time.sleep(15)  # Give it time to load

success = True

for group in groups:
    try:
        send_to_group(group, message)
    except Exception as e:
        print(f"Failed to send message to {group}: {e}")
        success = False

if success:
    log_run("Success")
else:
    log_run("Partial or Total Failure")
