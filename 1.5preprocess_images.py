import os
from PIL import Image
import json

# function: preprocess_image(input_path, output_path)
def preprocess_image(input_path, output_path):
    # open image with PIL
    img = Image.open(input_path)
    # convert to RGB
    img = img.convert("RGB")
    # resize
    img = img.resize((224, 224))
    # save to output path # force .jpg extension
    output_path = os.path.splitext(output_path)[0] + ".jpg"
    img.save(output_path, "JPEG")


# function: update_manifest_status(filename)
def update_manifest_status(filename):
    # load manifest
    file_path = "data/manifest.json"
    with open (file_path, "r") as f:
        manifest = json.load(f)

    # find entry by filename
    for image in manifest["images"]:
        if image["filename"] == filename:
            image["status"] = "processed"
            break

    # save manifest
    with open(file_path, "w") as f:
        json.dump(manifest, f, indent=2)

if __name__ == "__main__":
    raw_dir = "data/raw"
    processed_dir = "data/processed"
    
    # add this line
    actors_to_process = ["keaton", "clooney", "kilmer"]
    
    for actor_name in os.listdir(raw_dir):
        # add this check
        if actor_name not in actors_to_process:
            continue
            
        actor_raw_path = os.path.join(raw_dir, actor_name)
        # ... rest of code