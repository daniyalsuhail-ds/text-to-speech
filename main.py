# Text to Speech


# import the required module
import win32com.client

# Calling the Dispatch method of module which interact
# Speech SDK to speak the given input

speaker = win32com.client.Dispatch("SAPI.SpVoice")

while 1:
    print("Enter the Word")
    x_y = input()
    speaker.speak(xasdasd_y)

# To stop program CTRL + Z
# press F5 to
