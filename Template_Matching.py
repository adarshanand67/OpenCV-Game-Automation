'''
What Is Template Matching?

template matching is the concept in digital image processing used to extract a location of a pattern which is present in the image .

it works somewhat close to a convolution.

Advantage:

1)It is very useful to extract small features in an image.

Disadvantage:

1)More the number of template matching performed slower will be the process

2)since convolution is a slow process performing on a large pixeled image can reduce the performance of the code

3)slows down your computer on consecutive running and hence not consistent

4)It depends on your processor speed greater it is the better


Though Template matching is not the best when comes to game automation doesnt mean it lies in the bottom end. It can be used to automate games with less patterns 

Some games like 
Karate chop kick -https://html5.gamedistribution.com/dcd1e2c947894c5d8e94f43c87258dc8/

Tower Boxer -https://www.addictinggames.com/action/tower-boxer

Dino Game (not to a good extent due to more rivals)

Parkour climb-https://www.addictinggames.com/action/parkour-climb(same problem as dino game)

Cookie clicker and more

We Create a Bot which at its best scored upto 2620 in the game of Karate chop kick.


'''
import keyboard
import cv2
import numpy as np
from time import sleep,time
import pyautogui
import mouse
from pynput.mouse import Button,Controller
import pyscreenshot as ImageGrab
'''
This code is built to work on a 1080*1920 screen . make sure to fullscreen the game before running. keyboard is used to recieve the input s and q , which will start and stop your execution of code so that your system doesn't crash or get stuck in a looooooop. 

pyautogui.pause is to prevent break interval for pyautogui library
'''

'''
The function performs the template matching

and extracts the obstacle
'''

def matchobstacle(flag,id):
    if flag:
       #extracts left side 
      scr=ImageGrab.grab(bbox =leftside)
      wood=leftwood
    else :
        #extracts right side
      scr=ImageGrab.grab(bbox =rightside)
      wood=rightwood
    #converting numpy and gray scale for faster calculation and numpy is support by opencv
    scr=np.array(scr)
    scr=cv2.cvtColor(scr,cv2.COLOR_BGR2GRAY)

    result=cv2.matchTemplate(scr,wood,cv2.TM_CCOEFF_NORMED)
    _,maxval,_,maxloc=cv2.minMaxLoc(result)

    cv2.rectangle(scr,maxloc,(maxloc[0]+leftwoodh,maxloc[1]+leftwoodw),(0,0,255),2)
    ##name='image/'+str(id)+'.png'
    ## cv2.imwrite(name,scr)
    '''
    ABOVE CODE  for extracting the image and create a video
    '''
    id+=1
    if maxval>0.6 :
        flag=not flag 
    return flag,maxloc

'''
Using Ms paint figured out the leftside and the rightside. Extract the left wood and right wood which is basically flipped to the other direction.It is better to use a gray scale image to get a close estimation and lowering calculations.
'''

pyautogui.PAUSE=0

print('Press s to start playing:')
print('Press q to quit playing:')
keyboard.wait('s')

id=0

leftside=(810,500,1010,700)

rightside=(1040,500,1240,700)

leftwood=cv2.imread('left.png',0)
rightwood=cv2.imread('right.png',0)

leftwoodw,leftwoodh=leftwood.shape
rightwoodw,rightwoodh=rightwood.shape

flag=1
id=0
#define mouse controller and based on the setting position based on flag
mouse = Controller()
while(1): 
    flag,maxloc=matchobstacle(flag,id)
    id+=1
    if(flag):
        mouse.position=(885,700)
    else:
        mouse.position=(1165,700)
    mouse.click(Button.left)
    
    sleep(0.045)
    if keyboard.is_pressed('q'):
        break

