# Code reference: https://code.likeagirl.io/finding-dominant-colour-on-an-image-b4e075f98097 

import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

def find_histogram(clt):
    """
    create a histogram with k clusters
    :param: clt
    :return:hist
    """
    numLabels = np.arange(0, len(np.unique(clt.labels_)) + 1)
    (hist, _) = np.histogram(clt.labels_, bins=numLabels)

    hist = hist.astype("float")
    hist /= hist.sum()

    return hist
def plot_colors2(hist, centroids):
    bar = np.zeros((50, 300, 3), dtype="uint8")
    startX = 0

    for (percent, color) in zip(hist, centroids):
        # plot the relative percentage of each cluster
        endX = startX + (percent * 300)
        cv2.rectangle(bar, (int(startX), 0), (int(endX), 50),
                      color.astype("uint8").tolist(), -1)
        startX = endX

    # return the bar chart
    return bar

# Begin video capture before while loop. Otherwise, there will be lag in the video feed

cap = cv2.VideoCapture(0)

while (True):
    # ret is boolean (true or false), frame is the video dimensions (height, width)
    ret, frame = cap.read()

    # Get height and width of frame... 480 x 640
    frame_h, frame_w, channels = frame.shape

    # Set dimensions of rectangle to be drawn
    ## Top left corner is (0,0)... Top right corner is (w_max, h_max)
    rect_w = 100
    rect_h = 100
    x_start = int(frame_w / 2 - rect_w / 2)
    y_start = int(frame_h / 2 - rect_h / 2)
    x_end = x_start + rect_w
    y_end = y_start + rect_h

    # Draw the green rectangle 
    cv2.rectangle(frame, (x_start, y_start), (x_end, y_end), (0,255,0), 2)
    # Account for border thickness
    rect1 = frame[(y_start + 2):(y_end - 2), (x_start + 2):(x_end - 2)]  

    # Codelikeagirl
    img = cv2.cvtColor(rect1, cv2.COLOR_BGR2RGB)
    img = img.reshape((img.shape[0] * img.shape[1],3))  #represent as row*column,channel number
    clt = KMeans(n_clusters=3) #cluster number
    clt.fit(img)
    
    hist = find_histogram(clt)
    bar = plot_colors2(hist, clt.cluster_centers_)

    # # Display the bar... source code freezes up the video stream because it's plt.imshow, not ... 
    # # You must first convert back to BGR to show via cv2.imshow, not plt.imshow.
    ## Also, axis() and show() does NOT exist for in OpenCV 
    # plt.axis("off")
    # plt.imshow(bar)
    # plt.show()

    # Display the bar
    bar = cv2.cvtColor(bar, cv2.COLOR_RGB2BGR)
    cv2.imshow('Dominant Colors', bar)

    # Display the frame
    cv2.imshow('Video Screen',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print('Quitting Video Screen...')
        break

# After the break from while(true), Exit video stream. 
cap.release()
cv2.destroyAllWindows()