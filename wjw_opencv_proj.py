# from skimage.measure import compare_ssim
from skimage.metrics import structural_similarity as compare_ssim
import imutils
import cv2
import os
import numpy as np
import argparse
import pytesseract

#필요한 모듈 Import, 경로설정 부분 


# 설치한 tesseract 프로그램 경로 (64비트)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
# 32비트인 경우 => r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('before')
    parser.add_argument('after')
    return parser.parse_args()


def main():
    args = parse_args()
    imageA = cv2.imread(args.before)
    imageB = cv2.imread(args.after)
    
#반납 전 후 사진 파일 불러오는 부분 

    global roi
    global imageC
     
    
    #if needed resize images using cv2.resize()
    #cv2.imshow("before", imageA)
    #cv2.imshow("after", imageB)
    #cv2.waitKey(0)

    # 이미지 Gray 프로세싱
    #글자 인식 위해 gray 프로세싱하는 부분 

    grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
    grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
    
    (score, diff) = compare_ssim(grayA, grayB, full=True)
    diff = (diff * 255).astype("uint8")
    print(f"SSIM: {score}")
    #유사도 확인해 print 하는 부분 

    thresh = cv2.threshold(
                 diff, 0, 200, 
                 cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU
             )[1]
    cnts, _ = cv2.findContours(
                thresh, 
                cv2.RETR_EXTERNAL, 
                cv2.CHAIN_APPROX_SIMPLE
              )
    for c in cnts:
        area = cv2.contourArea(c)
        if area > 40:
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(imageA, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.drawContours(imageB, [c], -1, (0, 0, 255), 2)
#두 사진에서 다른 부분을 감지해 색으로 그려내는 부분 

    roi = imageA[y:y+h,x:x+w]
        
    imageC = roi.copy()

    imageC = "C:\Python310\wjw_opencv_proj\detect.jpg" # 이미지 경로

    img = cv2.imread(imageC, cv2.IMREAD_GRAYSCALE)
    
#두 사진에서 다른 부분을 감지해 이미지를 저장하는 부분
    
    
    # Simple image to string
    text = pytesseract.image_to_string(img, lang='kor')
    #글자인식 결과 한국어 인식해 출력 

    print(text)

    cv2.imshow("detect",img)
   
    cv2.imshow("before", imageA)
    cv2.imshow("after", imageB)
#책 대여 전 후, 책 제목 부분의 이미지 출력 

    cv2.waitKey(0)

if __name__ == "__main__":
        main()


# 1. 윈도우 키, cmd 실행

# 2.' cd C:\Python310\wjw_opencv_proj ' 입력 (파일 경로 입력)

# 3.' wjw_opencv_proj.py before.jpg after.jpg ' 입력 (실행할 파일,책 대여 이전 이후 사진 및 ocr 결과 출력)


# 'wjw_letter_opencv_proj.py' 입력 (지정된 사진의 ocr 원할 경우 실행. 이 프로젝트에선 사용하지 않음)


