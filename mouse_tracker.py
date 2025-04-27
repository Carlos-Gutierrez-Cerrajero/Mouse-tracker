###Mouse cursor tracker###
#Displays x, y coordinates and RGB color for cursor position (for GUI automation)
#Instructions:
#   Alt+R:  Save current cursor's position and color
#   Alt+S:  Save current cursor's position and color with input custom tag
#   Alt+L:  Write all saved positions and colors, with and without tag, to mouse_tracker_log.txt
#   Alt+Q:  With or without focused shell, quits program
#   Ctrl+C: With focused shell, quits program


##Imports
try:
    import logging
    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s.%(msecs)03d %(levelname)s: %(message)s",datefmt="%H:%M:%S")
    import time
    import pyautogui
    import keyboard
except ModuleNotFoundError:
    logging.critical ("Module not found, please make sure all required modules are installed")
    logging.info ("Press enter to Quit")
    input ("")
    exit()

##Functions
def dict_printer(dict, key_length):
    for key in list(dict.keys()):
        print (
        str(key).ljust(key_length)
        + str(dict[key][0]).rjust(4)
        + str(dict[key][1]).rjust(4)
        + str(dict[key][2]).rjust(4)
        + str(dict[key][3]).rjust(4)
        + str(dict[key][4]).rjust(4)
        )

def dict_writer(dict, key_length):
    for key in dict:
        log.write(
        str(key).ljust(key_length)
        + str(dict[key][0]) + ", "
        + str(dict[key][1]) + ", "
        + str(dict[key][2]) + ", "
        + str(dict[key][3]) + ", "
        + str(dict[key][4]) + "\n"
        )

##Code

print("")                                                                        #Prints and spaces instructions
logging.info("Press Alt+Q to quit")
logging.info("Press Alt+S to save with tag")
logging.info("Press Alt+R to save without tag")
logging.info("Press Alt+L to log saved positions")

print("")
logging.info("Current cursor coordinates and color:")

cursor_log={0:("x","y","r","g","b")}                                             #Initializes dictionaries
custom_log={"legend":("x","y","r","g","b")}

try:
    while True:                                                                  #Runs code within an infinite loop for sustained execution
        x, y = pyautogui.position()                                              #Gets current mouse position
        position_str = (                                                         #Formats position for readability
        "\t           X: " + str(x).rjust(4)
        + "  Y: " + str(y).rjust(4)
        )
        
        img=pyautogui.screenshot()                                               #Takes a screenshot
        color=img.getpixel((x, y))                                               #Gets the current cursor's position's color from the screenshot
        color_str = (                                                            #Formats color for readability
        "  |  R: " + str(color[0]).rjust(3)
        + "  G: " + str(color[1]).rjust(3)
        + "  B: " + str(color[2]).rjust(3)
        )
        
        erase_length = len(position_str) + len(color_str)                       #Calculates the length to be erased
        data=(x, y, color[0], color[1], color[2])                               #Formats tuple to store in dictionary
        
        print(position_str + color_str, end="")                                 #Prints position, without ending \n
        print("\b" * erase_length, end="", flush=True)                          #Erases last current position for the next loop iteration
        
        if keyboard.is_pressed("alt") and keyboard.is_pressed("s"):             #Detects Alt+S
            
            print("")                                                           #Spaces input so text doesn't glitch
            name = input("Insert name: ")                                       #Asks for tag name
            custom_log[name] = data                                             #Adds tag to dictionary
            
            print("")
            while keyboard.is_pressed("alt") or keyboard.is_pressed("s"):       #Waits for the release of Alt and S before continuing
                time.sleep(0.25)
        
        if keyboard.is_pressed("alt") and keyboard.is_pressed("r"):             #Detects Alt+R

            indexes = list(cursor_log.keys())                                   #Gets the dictionary keys
            indexes.sort()                                                      #Sorts dictionary keys in descending order
            next_index=indexes[-1] + 1                                          #Adds 1 to the last dictionary key
            cursor_log[next_index] = data                                       #Stores current data
            
            while keyboard.is_pressed("alt") or keyboard.is_pressed("r"):       #Waits for the release of Alt and R before continuing
                time.sleep(0.25)
        
        if keyboard.is_pressed("alt") and keyboard.is_pressed("l"):
            
            if len(cursor_log) <= 1 and len(custom_log) <= 1:                   #If the dictionaries are empty, skip this part
                continue
            
            log=open("mouse_tracker_log.txt","w")                               #Creates or overwrites mouse_tracker_log.txt
            
            if len(custom_log) > 1:
                log.write("Log of custom tags:\n\n")                            #Writes the title for the first dictionary and spaces it
                dict_writer(custom_log, 50)                                     #Loops through every dictionary item and writes it
                
                if len(cursor_log) > 1:
                    log.write("\n" + "-"*37 + "O" + "-"*37 + "\n")
            
            if len(cursor_log) > 1:
                log.write("\nLog of automatic tags:\n\n")                       #Writes the title for the second dictionary and spaces it
                dict_writer(cursor_log,5)                                       #Loops through every dictionary item and writes it
                    
            while keyboard.is_pressed("alt") or keyboard.is_pressed("l"):       #Waits for the release of Alt and L before continuing
                time.sleep(0.25)
        
        if keyboard.is_pressed("alt") and keyboard.is_pressed("q"):             #Breaks loop by pressing Alt+Q even on an unfocused winodw
            break

except KeyboardInterrupt:                                                       #Handles keyboard interruption to break out of the loop
    pass

print("\n")

if len(custom_log) > 1:                                                         #Prints both dictionaries formated
    dict_printer(custom_log, 50)
        
print("")

if len(cursor_log) > 1:
    dict_printer(cursor_log, 6)

print("")                                                                       #Prints and spaces out the finished message for readability
logging.info("Finished")

logging.info("Press enter to Quit")
keyboard.wait("enter")