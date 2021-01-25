# AUTOR Juan Manuel Camara Diaz
# EMAIL juanma.caaz@gmail.com
# Fecha 01/2021

# Programa para generar datos de entrenamiento para el modelo EAST
# Formato de salida del txt >> 1071,233,1138,228,1142,253,1072,259,###

import cv2 as cv
import os

class Points:
    def __init__(self):
        self.topLeft  = (-1,-1)
        self.topRight = (-1,-1)
        self.botRight = (-1,-1)
        self.botLeft  = (-1,-1)
        self.index    = 0

    def resetIndex(self):
        self.index = 0

    def isComplete(self):
        return self.index == 4

    def setPoint(self, points):
        if self.index == 0:   self.topLeft  = points; self.index += 1
        elif self.index == 1: self.topRight = points; self.index += 1
        elif self.index == 2: self.botRight = points; self.index += 1
        elif self.index == 3: self.botLeft  = points; self.index += 1

# Costantes

INPUT_DIR       = './input'
SELECTED_DIR    = './selected'

SCALE = 1

index = 0

def mouse_click(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        global index
        points.setPoint((int(x/SCALE),int(y/SCALE)))
        cv.circle(keyImgTemp, (x,y), 0, (255, 0, 0), 4)
        cv.putText(keyImgTemp, str(index), (0, 30), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv.LINE_AA)
        cv.imshow('main', keyImgTemp)
        print(x,y)

imgPaths = os.listdir(INPUT_DIR)

cv.namedWindow('main')
points = Points()
cv.setMouseCallback('main', mouse_click, points)

while index < len(imgPaths):

    path_img           = os.path.join(INPUT_DIR, imgPaths[index])
    path_outSelected   = os.path.join(SELECTED_DIR, imgPaths[index])
    path_outSelectedT  = os.path.join(SELECTED_DIR, imgPaths[index]).split('.jpg')[0] + '.txt'

    nextFrame = False
    keyImg = cv.imread(path_img)
    keyImgTemp = keyImg.copy()
    h, w, _ = keyImgTemp.shape
    keyImgTemp = cv.resize(keyImgTemp, (int(w*SCALE), int(h*SCALE)))

    while not nextFrame:
        cv.putText(keyImgTemp, str(index), (0, 30), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv.LINE_AA)
        cv.imshow('main', keyImgTemp)
        key = cv.waitKey(0)

        if key == ord('d'):

            if points.isComplete():
                f = open(path_outSelectedT, 'w')
                f.write(f'{points.topLeft[0]},{points.topLeft[1]},{points.topRight[0]},{points.topRight[1]},{points.botRight[0]},{points.botRight[1]},{points.botLeft[0]},{points.botLeft[1]},###')
                f.close()
                cv.imwrite(path_outSelected ,keyImg)

            points.resetIndex()
            index += 1
            nextFrame = True

        if key == ord('a'):
            index -= 1
            points.resetIndex()
            nextFrame = True

        if key == ord('r'):
            points.resetIndex()
            keyImgTemp = keyImg.copy()
            keyImgTemp = cv.resize(keyImgTemp, (int(w*SCALE), int(h*SCALE)))

        if key == ord('s'):
            exit(0)

    if index < 0: index = 0