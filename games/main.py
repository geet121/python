import pyautogui

from PIL import Image
import pyscreenshot as ImageGrab
import time
#from numpy import asarray#

def hit(key):
    pyautogui.keyDown(key)

def  isCollide(data):
    for i in range (580,596):
            for j in range (390,425):
                if data[i,j]< 100:
                    return True
    return False





if __name__ == "__main__":
    print("Hey...get ready to play in 3 secs")
    time.sleep(3)
    hit("up")

    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        if isCollide(data):
            hit("up")
        #print(asarray(image))  
        
            
        #image.show()
