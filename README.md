# woojaewon_opencv
woojaewon opencv project 

-프로그램 기본 설명 및 동작 과정-

도서관에서 책을 대여할 때, 책장의 위치로 대략적이게 알 수 있다.
따라서, 책장에서도 책이 꽂혀있는 정확한 위치를 찾기위해 제작된 프로그램이다. 

반납자는 책을 반납하기 전과 후 책장의 사진을 촬영한다. 이를 바탕으로 대여한 책의 위치의 후보를 찾아낸다.
해당 위치에서 글씨를 인식해 제목을 text로 출력한다. 다음 대여자가 프로그램을 실행하면 앞의 내용들이 수행되고. 
다음 대여자는 책을 쉽게 찾을 수 있다.

책 반납자 - 반납 전후로 책 제목에 맞게 책장 사진을 촬영, 이미지 파일로 저장한다. 

책 대여자 -  1. 책 반납자가 저장해둔 반납 전후 책장 사진 두 장을 찍는다.
               이를 before.jpg , after.jpg file로 포함해 프로그램을 실행한다. 
 
	          2. 프로그램은 알고리즘을 통해 before.jpg , after.jpg 간의 다른 부분을 탐지한다.
               (구현 방식은 , 책의 반납 전 후로 달라진 부분을 open cv 알고리즘을 활용하였다.) 
               
	   	      3. 2에서 탐지한 다른 부분은 책의 위치 후보에 해당하므로, 해당 부분을 detect.jpg 로 저장한다.
               detect.jpg 파일에 tesseract를 적용해 글자를 인식하여 제목을 찾는다.
               이를 사용자에게 출력하기 위해 text로 바꾸는 과정을 거친다.

  	        4. 변환된 text를 before.jpg , after.jpg, detect.jpg file들과 함께 출력한다.
               위의 과정을 통해 책 대여자가 정확한 책의 위치를 파악하도록 돕는다.


-구성-

folder 는 tessdata, jTEssBoxEditor,
file 은  before jpg. , after.jpg , detect.jpg , wjw_letter_opencv.proj , wjw_opencv_proj, wjw_opencv project file 이 들어있다. 

* tessdata
tesseract가 수행될 때 tessdata 의 data를 바탕으로 한다. 

* jTessbox Editor

jTessbox Editor은 tesseract를 학습시키는데 사용한 tool으로, 해당 프로젝트에서 사용한 버전은 jTessBoxEditor-2.0-Beta.zip과 같다. 

jTessBoxEditor 다운로드경로 https://sourceforge.net/projects/vietocr/files/jTessBoxEditor/

학습한 내용은 tessdata 파일에 넣는다. 이후 python 파일을 실행하면 tesseract 가 이를 반영해 결과를 출력할 것이다.  

* before jpg. , after.jpg , detect.jpg 는 각각 이전 반납자가 대여 전, 후 사진, 도출해낸 책의 위치 후보 사진이다.  

wjw_letter_opencv.proj 은 하나의 사진파일에서 글자인식을 하는 ocr 내용을 가지고 있는 python file 이다.
사진 하나만 넣고, 글자 인식 부분만 수행하길 원하는 경우를 위해 따로 분리해 두었다.
같은 내용이  wjw_opencv_proj에 포함되어 있는 파일으로, 프로젝트 실행엔 필요하지 않다. 

wjw_opencv_proj은 전체 내용을 포함하며 프로젝트에서 실행하는 파일이다.
사진 입력, 다른 부분 감지, 위의 글자인식 내용까지 포함한 내용을 가지고 있는 python file 이다.

-실행 방법- //wjw_opencv_proj.py의 가장 아래 주석으로도 포함되어 있다.

* 1. 윈도우 기준 , windows 키 + r 을 누르고, 확인을 눌러 cmd 창 실행 
* 2. ' cd C:\Python310\wjw_opencv_proj ' 입력 (파일 경로 입력)
* 3. ' wjw_opencv_proj.py before.jpg after.jpg ' 입력 (실행할 파일,책 대여 이전 이후 사진 및 ocr 결과 출력)

사진 하나만 넣고, 글자 인식 부분만 수행하길 원하는 경우
# 'wjw_letter_opencv_proj.py' 입력 (지정된 사진의 ocr 원할 경우 실행. 이 프로젝트에선 사용하지 않음)

원활한 이해를 위해 tesseract, cv2 jTessBoxEditor 에 대해 알아둔다.
나머지 내용은 code에 첨부된 주석에 설명해 두었다.
