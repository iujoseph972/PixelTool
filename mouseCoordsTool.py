import pyautogui,time

def getPixelLocation():
    position = pyautogui.position()
    print("x : " + str(position[0]) + " y: " +str(position[1]) )

def main():
    while True:
        getPixelLocation()
    
main()