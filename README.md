# 🟢 WhatsApp Group Reminder Automation (macOS)

A Python-based automation script that sends scheduled messages to specific WhatsApp groups via WhatsApp Web. Built for macOS and runs automatically using `launchd`.

---

## 📌 Features

- ✅ Sends daily reminders to selected WhatsApp groups  
- ✅ Skips Sundays  
- ✅ Automatically stops after a configurable date
- ✅ Displays a warning box for user to prepare for the automation
- ✅ Runs silently in the background using a `.plist` launcher  
- ✅ Logs execution output and errors for debugging  

---

## ⚙️ Requirements

- macOS  
- Python 3.x  
- [Google Chrome](https://www.google.com/chrome/)  
- [`pyautogui`](https://pypi.org/project/pyautogui/)  
- `launchd` (default macOS scheduling system)  

---

## 📦 Installation

1. **Clone this repo** or copy the files to your Mac.

2. **Install dependencies**:

   ```bash
   pip install pyautogui
   ```

3. **Enable screen control**:  
   Go to **System Preferences > Security & Privacy > Accessibility**, and allow Terminal or your Python app to control the screen.

4. **Update group names and message** in `scheduler.py`:

5. **Create or edit the shell script** `run_scheduler.sh`:

   Make it executable:

   ```bash
   chmod +x run_scheduler.sh
   ```

6. **Setup the Launch Agent (.plist)**

   Create a file at:

   ```
   ~/Library/LaunchAgents/com.user.whatsappreminder.plist
   ```

   And add your launch configuration:

   ```xml
   <?xml version="1.0" encoding="UTF-8"?>
   <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
   <plist version="1.0">
   <dict>
     <key>Label</key>
     <string>com.user.whatsappreminder</string>

     <key>ProgramArguments</key>
     <array>
       <string>/bin/bash</string>
       <string>/Users/your-username/Scripts/Whatsapp/run_scheduler.sh</string>
     </array>

     <key>StartCalendarInterval</key>
     <array>
       <dict><key>Hour</key><integer>20</integer><key>Minute</key><integer>0</integer></dict>
       <!-- Add more intervals as needed -->
     </array>

     <key>StandardOutPath</key>
     <string>/tmp/whatsapp_reminder.log</string>
     <key>StandardErrorPath</key>
     <string>/tmp/whatsapp_reminder.err</string>
   </dict>
   </plist>
   ```

7. **Load the launch agent**:

   ```bash
   launchctl load ~/Library/LaunchAgents/com.user.whatsappreminder.plist
   ```

---

## 📄 Logs

- Output: `/tmp/whatsapp_reminder.log`  
- Errors: `/tmp/whatsapp_reminder.err`

---

## 🧠 Notes

- Ensure WhatsApp Web is **already logged in** before automation starts.
- You may need to adjust the mouse click position in `send_message.py` based on your screen.
- Avoid interacting with mouse/keyboard while automation is running.

---

## 📅 Author

**Shrivatsa Naik**  
Built for personal use to automate daily WhatsApp group reminders.

---
