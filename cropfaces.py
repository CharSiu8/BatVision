import os
from PIL import Image
import cv2

# config
input_dir = "facestobecropped"
output_dir = "croppedfacesformodel"

# actors to process
actors = ["kilmer_google", "clooney_google", "keaton_google"]

def crop_face(image_path, output_path):
    # load image
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # load Haar cascade for face detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    # detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    
    if len(faces) > 0:
        # crop to first detected face
        (x, y, w, h) = faces[0]
        # padding
        # after (x, y, w, h) = faces[0]
        padding = int(w * 0.3)
        x = max(0, x - padding)
        y = max(0, y - padding)
        w = w + padding * 2
        h = h + padding * 2
        img_cropped = img[y:y+h, x:x+w]
        cv2.imwrite(output_path, img_cropped)
        print(f"Cropped: {output_path}")
    else:
        print(f"No face detected in: {image_path}")
 
if __name__ == "__main__":
    os.makedirs(output_dir, exist_ok=True)
    
    for filename in os.listdir(input_dir):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)
            crop_face(input_path, output_path)
    
    print("Done!")