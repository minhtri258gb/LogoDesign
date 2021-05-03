
import numpy as np
import cv2


# Color is RGBA
# thinkness = -1 : fill color

# define
eraseColor = (255,255,255,255)
drawColor = (0,0,0,255)
drawColor1 = (0,0,0,255) # color of out frame 145
drawColor2 = (0,0,0,255) # color of in frame 105

def drawPolyLines(img, list, color=drawColor, isClose=True):
	pts = np.array(list, np.int32)
	pts = pts.reshape((-1, 1, 2))
	return cv2.polylines(img, [pts], isClose, color, 1)

def drawPoint(img, pos):
	return cv2.circle(img, pos, 0, drawColor, -1)

def drawVerticalLine(img, y1, y2, listx):
	res = img
	for x in listx:
		res = cv2.line(img, (x,y1), (x,y2), drawColor, 1)
	return res

# Create empty image with 512 x 512 x 4
img = np.zeros([512, 512, 4], np.uint8)

# clear color with transparency
img = cv2.rectangle(img, (0, 0), (511, 511), eraseColor, -1)

# head
img = cv2.circle(img, (256,240), 74, drawColor, 1) # out
img = cv2.circle(img, (256,240), 68, drawColor, 1) # in
img = cv2.rectangle(img, (191,276), (321, 314), eraseColor, -1) # xoa phan lon
img = cv2.rectangle(img, (197,273), (315, 275), eraseColor, -1) # xoa phan nho

# face
img = cv2.ellipse(img, (128,128), (123,172), 0, 0, 90, drawColor, 1) # left out
img = cv2.ellipse(img, (128,128), (129,178), 0, 0, 90, drawColor, 1) # left in
img = cv2.ellipse(img, (384,128), (123,172), 0, 90, 180, drawColor, 1) # right out
img = cv2.ellipse(img, (384,128), (129,178), 0, 90, 180, drawColor, 1) # right in
img = cv2.rectangle(img, (128,282), (384,306), eraseColor, -1) # erase bottom
img = cv2.rectangle(img, (247,128), (265,193), eraseColor, -1) # erase top

# mount
imp = drawPolyLines(img, [[183,282],[183,296],[329,296],[329,282]], isClose=False) # out
img = cv2.line(img, (194,282), (318,282), drawColor, 1) # in

# nose
img = cv2.line(img, (249,194), (263,194), drawColor, 1) # top

# horn
img = drawVerticalLine(img, 152, 156, [250, 256, 262])
img = drawVerticalLine(img, 157, 161, [249, 251, 255, 257, 261, 263])
img = drawVerticalLine(img, 162, 166, [248, 252, 254, 258, 260, 264])
img = drawVerticalLine(img, 167, 172, [247, 253, 259, 265])
img = drawVerticalLine(img, 173, 178, [246, 266])

# Frame
img = drawPolyLines(img, [[256,84],[144,256],[256,428],[368,256]], drawColor2) # main
img = drawPolyLines(img, [[100,256],[212,84],[223,101],[122,256],[223,414],[212,428],[100,256]], drawColor1) # left
img = drawPolyLines(img, [[412,256],[300,84],[289,101],[390,256],[289,414],[300,428],[412,256]], drawColor1) # right

# Convert default BGRA to RGBA
img = cv2.cvtColor(img, cv2.COLOR_BGRA2RGBA)

output = 2
if output != 1:
	cv2.imwrite('logo.png', img) # write to file
if output != 2:
	cv2.imshow('image', img) # show image
	cv2.waitKey(0) # press any to continue
	cv2.destroyAllWindows() # close window