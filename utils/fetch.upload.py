import requests
from utils.azure_blob import AzureBlobService
import json

def fetch_data_upload_blob(api_url, blob_name):
    response = requests.get(api_url)
    response.raise_for_status()
    data = response.json()

    azure_service = AzureBlobService()
    azure_service.upload_data(json.dumps(data), blob_name)
