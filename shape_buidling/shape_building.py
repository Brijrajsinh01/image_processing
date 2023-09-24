import cv2 as cv
import numpy as np

# Create a blank image with a white background
width, height = 800, 600
blank_image = np.zeros((height, width, 3), np.uint8)
blank_image.fill(255)  # Fill with white color (255, 255, 255)

color =( 0,0,255)
thickness = 2
start_point=(10,10)
end_point= (100 ,10 )
cv.line(blank_image,start_point,end_point,color,thickness)

vertices = np.array([[400, 100], [600, 300], [200, 300]], np.int32)

# Reshape the vertices array to a shape that OpenCV expects
vertices = vertices.reshape((-1, 1, 2))

# Draw the triangle
color = (0, 0, 255)  # BGR color format (red)
thickness = 2
cv.polylines(blank_image, [vertices], isClosed=True, color=color, thickness=thickness)

amplitude = 100
frequency = 0.02  # Adjust this value to change the frequency of the sine wave
phase = 0
for x in range(width):
    y = int(amplitude * np.sin(2 * np.pi * frequency * x + phase) + height / 2)
    cv.circle(blank_image, (x, y), thickness, color, -1)

cv.imshow('Blank Image', blank_image)
cv.waitKey(0)