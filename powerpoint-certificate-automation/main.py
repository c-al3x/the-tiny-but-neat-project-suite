import time
import pyautogui

def start_certificate_process():
  pyautogui.press("winleft")
  pyautogui.typewrite("10-certificate-template-powerpoint_002")
  time.sleep(1)
  pyautogui.press("enter")
  time.sleep(3)
  pyautogui.press("enter")
  pyautogui.press(["tab" for _ in range(6)], interval=0.5)

def make_certificate(name):
    pyautogui.press("enter")
    pyautogui.hotkey("ctrl", "a")
    time.sleep(1)
    pyautogui.press("backspace")
    time.sleep(1)
    pyautogui.typewrite(name)
    time.sleep(1)
    pyautogui.press("f12")
    time.sleep(1)
    pyautogui.typewrite(name)
    time.sleep(1)
    pyautogui.press("tab")
    time.sleep(1)
    pyautogui.press(["down" for _ in range(40)])
    time.sleep(1)
    pyautogui.press(["up" for _ in range(8)])
    time.sleep(1)
    pyautogui.press(["enter", "enter"])
    time.sleep(1)
    pyautogui.press(["right", "enter"])
    time.sleep(1)

def main():
    restarting = 0
    while (1):
      names = []
      if (not restarting):
        pyautogui.alert(text='Enter each name individually that you would like to ' +
        'make a certificate for. Once you are done entering all the names, click ' +
        'the cancel button. When all certificates are done, a final message will ' +
        'display.', title='Welcome', button='OK')
      started = 0;
      while (not started):
        first_name = pyautogui.prompt("Enter a name.")
        if (not first_name):
          next_response = pyautogui.confirm(text="Would you like to quit the program?",
          title="Ready To Quit", buttons=["Yes", "No"])
          if (next_response == "Yes"):
            pyautogui.alert(text="Quitting program. Goodbye!", title="Final Message", button="OK")
            return 1
        else:
          names.append(first_name)
          started = 1
      while (1):
        curr_name = pyautogui.prompt("Enter another name. Click 'Cancel' if done entering names.")
        if (not curr_name):
          break
        names.append(curr_name)
      response = pyautogui.confirm(text="All certificates will start to be created. " +
      "Proceed?", title="Certification Process Ready", buttons=["Yes", "No"])
      if (response == "No"):
          next_response = pyautogui.confirm(text="Would you like to quit the program?",
          title="Ready To Quit", buttons=["Yes", "No"])
          if (next_response == "Yes"):
            pyautogui.alert(text="Quitting program. Goodbye!", title="Final Message", button="OK")
            break
      else:
        if (not restarting):
          start_certificate_process()
        for name in names:
          make_certificate(name)
        final_response = pyautogui.confirm(text="All certificates were created! " +
                        "Would you like to make more certificates?",
                        title="Certificates Finished", buttons=["Yes", "No"])
        if (final_response == "No"):
          pyautogui.alert(text="Quitting program. Goodbye!", title="Final Message", button="OK")
          return 1
        else:
          restarting = 1

if __name__ == "__main__":
   main()

