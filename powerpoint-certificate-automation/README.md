# Powerpoint Certificate Automation

This script automates the process of creating a large set of certificates with the provided PowerPoint template.

WARNING: This script takes control of your keyboard and mouse. I would suggest you do not run this script, but if you do, you
need to be running the Windows operating system and have the provided PowerPoint template in your home directory. Even then, there
might be negative consequences. I am not responsible for any damage as a result of running this script.

I created this script specifically for my mom. It runs perfectly fine on her computer, which runs Windows 10 and contains the provided PowerPoint template
in her home directory. I have not tested this script on any other machine.

I have no clue why you would want to run this script, but if you do, please heed the warning above. Automating PowerPoint projects is
tricky, because you can only interact with the software through a graphical user interface. You cannot simply run a shell script. 
This is why I had to rely on the pyautogui library, which takes control of the user's keyboard and mouse.
