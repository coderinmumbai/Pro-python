import pyautogui as spam 
import time 
limit=input("enter the number")
msg=input("enter msg ")
i=0
time.sleep(5)
while i<int(limit):
    spam.typewrite(msg)
    spam.press("enter")
    i+=1