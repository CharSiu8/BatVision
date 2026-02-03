import gradio as gr
import requests
import os
from dotenv import load_dotenv
from PIL import Image
from io import BytesIO

# load environment variables
load_dotenv()

print("ENV CHECK:")
print(f"Endpoint length: {len(os.getenv('CUSTOM_VISION_ENDPOINT', ''))}")
print(f"Key length: {len(os.getenv('CUSTOM_VISION_KEY', ''))}")
# config: endpoint, key
CUSTOM_VISION_ENDPOINT = os.getenv("CUSTOM_VISION_ENDPOINT")
CUSTOM_VISION_KEY = os.getenv("CUSTOM_VISION_KEY")
if not CUSTOM_VISION_ENDPOINT:
    print("Error: CUSTOM_VISION_ENDPOINT not set in .env")
    exit(1)
if not CUSTOM_VISION_KEY:
    print("Error: CUSTOM_VISION_KEY not set in .env")
    exit(1)
print("Endpoint:", CUSTOM_VISION_ENDPOINT)
print("Key:", CUSTOM_VISION_KEY[:10] + "...")
# function: predict(image)
def predict(image):
    # create a BytesIO buffer
    buffer = BytesIO()
    
    # use PIL Image to open the image
    img = Image.open(image)
    
    # save image to buffer as JPEG
    img.save(buffer, format="JPEG")
    
    # get bytes using buffer.getvalue()
    image_bytes = buffer.getvalue()
    
    # send POST request to Custom Vision API
    headers = {
        "Prediction-Key": CUSTOM_VISION_KEY,
        "Content-Type": "application/octet-stream"
    }
    response = requests.post(CUSTOM_VISION_ENDPOINT, headers=headers, data=image_bytes)
    
    # parse response
    result = response.json()
    print(result)
    predictions = result["predictions"]
    top = max(predictions, key=lambda x: x["probability"])
    
    # return top prediction + confidence
    name = top["tagName"].capitalize()
    confidence = top["probability"] * 100
    return f"{name} ({confidence:.1f}% confidence)"

# interface
demo = gr.Interface(
    fn=predict,
    inputs=gr.Image(type="filepath"),
    outputs=gr.Text(label="Prediction"),
    title="BatVision",
    description="Upload an image of Batman to identify the actor. Accepts: Affleck, Bale, Pattinson, Nite Owl, Darkwing."
)

# launch
demo.launch()