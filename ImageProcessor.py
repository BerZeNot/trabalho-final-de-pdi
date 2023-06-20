import cv2
import pytesseract

def extractText(imageName):
    print("Extracting text from:", imageName)
    img = cv2.imread(imageName)
    # img = cv2.resize(img, None, fx=0.5, fy=0.5)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    new_image = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 85, 11)
    text = pytesseract.image_to_string(new_image, config="--psm 3")
    return text