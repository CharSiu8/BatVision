import os
from ddgs import DDGS
import json
import requests
import time
from datetime import datetime

# config: list of actors + search queries
actors = {
    "afleck": "Ben Afleck Batman costume",
    "bale": "Christian Bale Batman costume",
    "pattinson": "Robert Pattinson Batman Costume",
    "niteowl": "Niteowl Watchmen costume"
}

# download_image(url, save_path)
def download_image(url, save_path):
    # try block starts here
    try: 
        # requests.get(url, timeout=10) — fetches the image
        response = requests.get(url, timeout = 10)
        # check if response.status_code == 200
        if response.status_code == 200:
            with open(save_path, "wb") as file:
                file.write(response.content)
            print("Image successfully downloaded: downloaded_image.jpg")
            return True
        else:
            print(f"Failed to retrieve image. Status code: {response.status_code}")
            return False
    except Exception as e:
        print(f"Error downloading: {e}")
        return False

# function: update_manifest(image_data)
def update_manifest(image_data):
    file_path = "data/manifest.json"
    # load manifest.json
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            try:
                manifest = json.load(f)
            except json.JSONDecodeError:
                manifest = {"images": [], "metadata": {"total_images": 0}}
    else:
        manifest = manifest = {"images": [], "metadata": {"total_images": 0}}
    
    # append new image entry
    manifest["images"].append(image_data)
    # update metadata count
    manifest["metadata"]["total_images"] += 1
    # save manifest.json
    with open(file_path, "w") as f:
        json.dump(manifest, f, indent=2)

# function: collect_for_actor(actor_name, search_query, num_images)
def collect_for_actor(actor_name, search_query, num_images):
    """ Searches DuckDuckGO for images and collects URLs for specific actors """
    image_links = []

    # search DDG for query
    with DDGS() as ddgs:
        results = ddgs.images(
    query=search_query,
    max_results=num_images
)
    # loop through results
    for result in results:
        image_links.append(result.get("image"))

    # loop through image_links with index
    try:
        os.makedirs(os.path.join("data", "raw", actor_name), exist_ok=True)
    except FileExistsError:
        pass
    for index, image_link in enumerate(image_links):
        save_path = os.path.join("data", "raw", actor_name, f"{actor_name}_{index:03d}.jpg")

        success = download_image(image_link, save_path)

        if success:
            image_data = {
                "filename": f"{actor_name}_{index:03d}.jpg",
                "actor": actor_name,
                "source_url": image_link,
                "date_collected": datetime.now().strftime("%Y-%m-%d"),
                "dimensions": [224, 224],
                "status": "raw"
            }
            update_manifest(image_data)
        time.sleep(2) # slowing down the process to avoid getting blocked by DuckDuckGo

    return {
        "actor": actor_name,
        "search_query": search_query,
        "image_urls": image_links
    } 

# main: loop through all actors
    # call collect_for_actor for each
    # print summary when done
if __name__ == "__main__":
    num_images = 5  # per actor
    
    for actor_name, search_query in actors.items():
        print(f"Collecting {num_images} images for {actor_name}...")
        collect_for_actor(actor_name, search_query, num_images)
    
    print("Done!")