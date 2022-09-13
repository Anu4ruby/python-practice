#https://thecleverprogrammer.com/2021/06/26/text-to-handwriting-using-python/
#pip install pywhatkit
import pywhatkit as kit
import cv2

kit.text_to_handwriting("hello world", save_to="text_to_handwriting.png")
img = cv2.imread("text_to_handwriting.png")
cv2.imshow("Text to Handwriting", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
