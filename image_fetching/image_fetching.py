import cv2
import numpy as np
import urllib.request

# Define the URL of the online image you want to render
image_url = "http://192.168.29.9:8080/shot.jpg "

# Download the image from the URL
response = urllib.request.urlopen(image_url)
image_array = np.asarray(bytearray(response.read()), dtype=np.uint8)

# image_pc = cv2.imread('online_image.jpg')
# Decode the downloaded image
image = cv2.imdecode(image_array, -1)

# Specify the new dimensions (width and height)
new_width = 960
new_height = 540

# Resize the image using the cv2.resize() function
resized_image = cv2.resize(image, (new_width, new_height))


gray = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
edges = cv2.Canny(gray, 50, 150)
contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# print(contours)
for contour in contours:
    # epsilon = 0.04 * cv2.arcLength(contour, True)
    # approx = cv2.approxPolyDP(contour, epsilon, True)
    
    # If the contour has 4 vertices, it's likely a rectangle (or a box)
    if len(contour) > 300:
        cv2.drawContours(resized_image, contours, -1, (0, 255, 0), 1)  # Draw the contour on the original image

cv2.imshow("gray Image", gray)
cv2.imshow("blurred Image", blurred)
cv2.imshow("edge Image", edges)
# cv2.waitKey(0)
cv2.imshow("Online Image", resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# # Save the image (optional)
# cv2.imwrite("online_image.jpg", image_pc)
