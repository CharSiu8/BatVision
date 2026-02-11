from mtcnn import MTCNN
import cv2
import os

# add relevant files first ( for each batman) 

detector = MTCNN()

for img_file in os.listdir('batman_images/'):
    img = cv2.imread(f'batman_images/{img_file}')
    faces = detector.detect_faces(img)
    
    if faces:
        x, y, w, h = faces[0]['box']
        face = img[y:y+h, x:x+w]
        cv2.imwrite(f'cropped_faces/{img_file}', face)
