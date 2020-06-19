import pyautogui
import time

message = "add your message in the quotaion"

time.sleep(5) #waits 5 secs to find input box

while True:
  pyautogui.write(message)
  time.sleep(1) #remove if you want to make it faster
  pyautogui.press("enter")
