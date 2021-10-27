import pyautogui, webbrowser
from time import sleep

# include your country code and no spaces
# phone = 'YOUR_PHONE_HERE'

# open whatsapp web input ej: +(location id)# , +50465365456 , 504 = location id : 65365456 = phone number
val = input("Enter your phone number(ej: +50465365456 , +504 = location id : 65365456 = phone number): ")
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

