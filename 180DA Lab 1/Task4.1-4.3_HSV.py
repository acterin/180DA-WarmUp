import cv2
import numpy as np

# Set the HSV range for the blue object
lower_hsv = np.array([100, 50, 50])
upper_hsv = np.array([130, 255, 255])

# Open the video stream
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the video stream
    ret, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv_frame, lower_hsv, upper_hsv)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        # Get the largest contour
        largest_contour = max(contours, key=cv2.contourArea)
        
        # Get the bounding box for the contour
        x, y, w, h = cv2.boundingRect(largest_contour)
        
        # Draw the bounding box on the frame
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
    # Display the frame with the bounding box
    cv2.imshow("Object Tracking (HSV)", frame)
    
    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print('Quitting Video Screen...')
        break

# Release the video stream and close all windows
cap.release()
cv2.destroyAllWindows()