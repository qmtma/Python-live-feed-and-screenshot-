# make sure you install Opencv
# run this command on python terminal" pip install opencv-python "
import cv2  # importing Opencv extension allowing frame and video capture
import os  # built ins python function implemented here to allow custom directory(image save location)

print("Live feed launching")  # line 3-5 user guide
print("press \"esc\" to exit program")
print("press \"spacebar\" to capture frame")
# defining feed input. 0 for laptop built in camera storing its address to (capture)variable
capture = cv2.VideoCapture(0)
count = 0  # count declaration (controls screenshot numbering)

# accessing change directory function from os library. the argument is the location
# path in which screenshots are saved.\n
# recommended "C:\Users\{enter your default user(in my case it was qmtma)}\Pictures.
# or any folder desired its really up to you.
os.chdir(r"C:\Users\qmtma\Pictures")

while True:  # infinite loop allowing continuous frame read and display (capturing video frame by frame)
    ret, vid = capture.read()
    # capture.read() is a Opencv function checking if a frame has been captured.
    # vid variable will contain the frame if the read() returned true.
    # ret will be 0 if read() returned false
    cv2.imshow("WebCam", vid)
    # launching a window named "WebCam" containing the obtained frame from the read function
    # cv2.imshow(window_name, frame_variable)
    if cv2.waitKey(1) == 32:
        # cv2.waitkey(1) waits for a button press from the keyboard the condition here check if its equal to 32(the
        # ASCII code for the spacebar) its a given u can change it to any button if you know the ASCII
        cv2.imwrite(f"screenshot{count}.jpg", vid)
        # cv2.imwrite() saves the captured frame to the compiler running directory, which in this case has been modified
        # in line 15. function prototype cv2.imwrite(filename, frame_variable)
        count += 1 # count increment after each screenshot. (giving each screenshot its own number)
        print("your pressed \'SpaceBar\' , screenshot captured")
    elif cv2.waitKey(1) == 27:
        # if the user doesnt press spacebar, and the "esc" button is pressed then the loop will terminate
        print("Terminating program")
        break
        # break command closing the infinite will loop
cv2.destroyAllWindows()
# closes all windows created using imshow()
