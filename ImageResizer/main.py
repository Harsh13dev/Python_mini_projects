import cv2

#Configurable Parameters
source = "class.png"
destination = 'ResizedImage.png'
scale_percent = 50


image = cv2.imread(source , cv2.IMREAD_UNCHANGED)
#cv2.imshow("title", image)

#calculate the 50 percent of original dimensions
width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)

# resize image
output = cv2.resize(image, (width, height))

cv2.imwrite(destination , output)
