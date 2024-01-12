import cv2
import numpy as np

# Function to track the object in the video stream
def track_object():
    cap = cv2.VideoCapture(0)  # 0 for default camera, you can change it if needed

    # Define the HSV range for your object (adjust these values based on your object's color)
    lower_color = np.array([hue_min, saturation_min, value_min])
    upper_color = np.array([hue_max, saturation_max, value_max])

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Convert the frame to HSV color space
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Threshold the frame based on the color range
        mask = cv2.inRange(hsv_frame, lower_color, upper_color)

        # Find contours in the thresholded image
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Draw bounding box around the object
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Display the result
        cv2.imshow('Object Tracking', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Define the HSV range for your object (adjust these values based on your object's color)
hue_min, saturation_min, value_min = 30, 50, 50
hue_max, saturation_max, value_max = 60, 255, 255

# Start object tracking
track_object()

