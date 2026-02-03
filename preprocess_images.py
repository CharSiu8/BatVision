import os
import PIL import Image
import json

# function: preprocess_image(input_path, output_path)
def preprocess_image(input_path, output_path):
    # open image with PIL
    img = Image.open(input_path)
    # convert to RGB
    img = img.convert("RGB")
    # resize
    img = img.resize((224, 224))
    # save to output path
    img.save(output_path)


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
    
    # loop through each actor folder in /raw
    for actor_name in os.listdir(raw_dir):
        actor_raw_path = os.path.join(raw_dir, actor_name)
        actor_processed_path = os.path.join(processed_dir, actor_name)
        
        # create matching folder in /processed
        os.makedirs(actor_processed_path, exist_ok=True)
        
        # loop through images
        for filename in os.listdir(actor_raw_path):
            input_path = os.path.join(actor_raw_path, filename)
            output_path = os.path.join(actor_processed_path, filename)
            
            # call preprocess_image
            preprocess_image(input_path, output_path)
            
            # call update_manifest_status
            update_manifest_status(filename)
            
            # print progress
            print(f"Processed: {filename}")
    
    print("Done processing images!")