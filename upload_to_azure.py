import os
from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv

# load environment variables
load_dotenv()

# config: connection string, container name
connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
container_name = "images"
if not connection_string:
    print("Error: AZURE_STORAGE_CONNECTION_STRING not set in .env")
    exit(1)

# function: upload_folder(folder_path, actor_name)
def upload_folder(folder_path, actor_name):

    # get blob service client
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    container_client = blob_service_client.get_container_client(container_name)
    # loop through files in folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

    # upload each file as blob (path: actor_name/filename)
        blob_name = f"{actor_name}/{filename}"
        with open (file_path, "rb") as data:
            container_client.upload_blob(name=blob_name, data=data, overwrite = True)

        print(f"Uploaded: {blob_name}")

# main: loop through each actor in /processed
if __name__ == "__main__":
    processed_dir = "data/processed"
    
    for actor_name in os.listdir(processed_dir):
        folder_path = os.path.join(processed_dir, actor_name)
        upload_folder(folder_path, actor_name)
    
    print("Upload complete!")
    