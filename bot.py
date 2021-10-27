import pyautogui, webbrowser
from time import sleep

# include your country code and no spaces
# phone = 'YOUR_PHONE_HERE'

# open whatsapp web +50496047044  +50496672751  +5218117877078 +50433061272 +50494612026  +50496742099 +50431771770 +50496476366 +50432269370 +50499159502
val = input("Enter your value: ")
print(val)
ruta = "https://web.whatsapp.com/send?phone="
res=ruta+val;
print(res)

webbrowser.open(res)
sleep(5)

# open a simple file
#try:
while 1:
 with open('song.txt','r') as file:
    # iterate
    for line in file:
        # write the lines on page opened
        pyautogui.typewrite(line)

        # press enter (send message)
        pyautogui.press("enter")
#except KeyboardInterrupt:
   # pass

