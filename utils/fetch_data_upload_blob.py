from utils.azure_blob import AzureBlobService
import json


def fetch_data_upload_blob(api_url,blob_name):
    data=fetch_data_upload_blob(api_url)

    azure_service=AzureBlobService()
    azure_service.upload_data(json.dumps(data),blob_name)