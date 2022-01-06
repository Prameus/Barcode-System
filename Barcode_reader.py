import xlsxwriter
from pyzbar.pyzbar import decode
import cv2
import numpy


cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(3, 640)
cap.set(4, 480)


def barcode_reader():
    while True:
        success, img = cap.read()
        for barcode in decode(img):
            print(barcode.data)
            myData = barcode.data.decode('utf-8')
            print(myData)
            pts = numpy.array([barcode.polygon], numpy.int32)
            pts = pts.reshape((-1, 1, 2))
            cv2.polylines(img, [pts], True, (255, 0, 255), 5)
            pts2 = barcode.rect
            cv2.putText(img, myData, (pts2[0], pts2[1]),
                        cv2.FONT_HERSHEY_COMPLEX, 0.9, (255, 0, 255), 2)

        cv2.imshow('result', img)
        cv2.waitKey(1)

barcode_reader()