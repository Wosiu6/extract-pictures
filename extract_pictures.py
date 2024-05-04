import cv2
import os

print("This application extracts rectangle images from any picture. See example on https://github.com/Wosiu6")
photo_path = input("Photo path: ")
output_directory = input("Output directory: ")

original_image = cv2.imread(photo_path, cv2.IMREAD_UNCHANGED)

greyscale_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
gradient = cv2.morphologyEx(greyscale_image, cv2.MORPH_GRADIENT, kernel)

target_image_contours = cv2.findContours(gradient, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[1]

counter = 0

for target_image in target_image_contours:
    counter = counter + 1
    (x,y,w,h) = cv2.boundingRect(target_image)

    target_path = os.path.join(output_directory, output_directory + "_" + str(counter) + ".png")

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    roi = original_image[y:y+h, x:x+w]
    cv2.imwrite(target_path, roi)