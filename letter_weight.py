import cv2
import numpy as np

#import image
pikletter = cv2.imread(r'C:\Users\soarh\Desktop\opendyslexic.png')
cv2.imshow('pikletter', pikletter)

#check image size
height, width, channels = pikletter.shape
print(height) #95
print(width) #83
print(channels)

#grayscale image
graypik = cv2.cvtColor(pikletter, cv2.COLOR_BGR2GRAY)
rows, cols = graypik.shape
resultx = 0
resulty = 0
mass = 0

#calculate center of mass
for i in range (rows):
    for j in range(cols):
        k = graypik[i,j]
        resultx += (255-k)*j
        resulty += (255-k)*i
        if 255-k > 0:
            mass+=255-k

resultx /= mass
resulty /= mass

print("(", resultx,",", resulty, ")")

#calculate percentage height of CoM
intresultx = int(resultx)
intresulty = int(resulty)
realheight = height
realcheck = 0
falseup = 0

#check from up
for i in range (rows):
    realcheck = 0
    for j in range(cols):
        k=graypik[i,j]
        if 255-k > 0:
            realcheck = 1
    if realcheck == 0:
        realheight -= 1
        falseup+=1
    elif realcheck == 1:
        break
#check from down
for i in range (rows-1,0,-1):
    realcheck = 0
    for j in range(cols):
        k=graypik[i,j]
        if 255-k > 0:
            realcheck = 1
    if realcheck == 0:
        realheight -= 1
    elif realcheck == 1:
        break
getheight = (resulty-falseup) / realheight
print("%4.2f" %getheight)

#show image with line on CoM
cv2.line(pikletter, (0, intresulty), (width, intresulty), (255,255,0), 1)
cv2.imshow('open dyslexic', pikletter)

