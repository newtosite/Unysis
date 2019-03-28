import cv2,os
import numpy as np
font = cv2.FONT_HERSHEY_SIMPLEX
print("Scan license...")
					
cam = cv2.VideoCapture(0)
ch='continue';
while ch!='stop':
	ret,im=cam.read()
	cv2.imshow('im',im)
	if cv2.waitKey(1)== ord('q'): 
		cv2.imwrite("demo.jpg", im)
		ch='stop'
		break;							
cam.release()
cv2.destroyAllWindows()
					
from PIL import Image 
image = Image.open('demo.jpg')	
greyscale_image = image.convert('L')
greyscale_image.save('demog.jpg');	
img = cv2.imread('demog.jpg')
b,g,r = cv2.split(img)          
rgb_img = cv2.merge([r,g,b])  
dst = cv2.fastNlMeansDenoisingColored(img,None,10,10,7,21)
b,g,r = cv2.split(dst)           
rgb_dst = cv2.merge([r,g,b])    
cv2.imwrite('demogv.jpg',rgb_dst)
try:
	from PIL import Image
except ImportError:
	import Image
import pytesseract
licence =  ['licencing','dl','valid','india','mcwg','lmv','name','till','throughout','16(2)','bg','doi','cov','dob']
rc = ['reg','chassis','engine','mfr','class','registering','colour','ownername','s/w/d','model','body','wheel','base','23A','mfg','fuel','tax','seating','cc']
rcCounter = 0
licenceCounter = 0
foo = pytesseract.image_to_string(Image.open('C:\\Users\\pc\\python programs\\demog.jpg'))
x = open("demogv.txt","w")
for word in foo:
	if ( word.isalpha() or word.isdigit() or word == '/' or word == '(' or word == ')'): #if(word == ':' or word == '.' or word == '!' or word == '/' or word == '-' or word == '[' or word == '>' or word == '@' or word == '=' ):
		x.write("%s" %word)
	elif(word == " "):
		x.write("\n")
	else:
		x.write("\n")		
x.close()
file = open("demogv.txt","r")
for line in file:
	line = line.strip()
	line = line.lower()
	if line in licence:
		licenceCounter = licenceCounter+1	
	if line in rc :
		rcCounter = rcCounter+1		
if licenceCounter > rcCounter :
	print ( " \nTHE DOCUMENT IS A LICENSE ")
	chrome_path='C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
	webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path),1)
	webbrowser.get('chrome').open_new_tab('http://localhost/kpit/telematic_main.html')
elif licenceCounter < rcCounter:
	print ( " the document is a rc ")
else:
	print(" THE DOCUMENT IS NOT A VALID LICENSE ")
file.close()
exit()