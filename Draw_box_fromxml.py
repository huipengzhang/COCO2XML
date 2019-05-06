#coding:utf-8
import cv2
import xml.etree.cElementTree as ET

image = './0.jpg'
x_file = './0.xml'


image = cv2.imread(image)
#cv2.imshow(image)

tree = ET.parse(x_file)
root = tree.getroot()

for child in root[4][4]:
    print(child.text)


xmin = root[5][4][0].text
ymin = root[5][4][1].text
xmax = root[5][4][2].text
ymax = root[5][4][3].text

print(root[4][4][2].text)

xy = [int(xmin), int(ymin), int(xmax), int(ymax)]

r_image = cv2.rectangle(image, (xy[0], xy[1]), (xy[2], xy[3]), (255, 0, 0), 2)  # kare çiz

cv2.imshow("rectangle", r_image)


cv2.waitKey(0)
cv2.imwrite('test.jpg', r_image)
cv2.destroyAllWindows()
