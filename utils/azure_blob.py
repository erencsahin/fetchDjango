from azure.storage.blob import BlobServiceClient
from django.conf import settings
import os

class AzureBlobService:
    def __init__(self):
        connection_string = settings.AZURE_CONNECTION_STRING_DEV if os.getenv('DJANGO_ENV') != 'production' else settings.AZURE_CONNECTION_STRING_PROD
        container_name = settings.AZURE_CONTAINER_NAME
        self.blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        self.container_client = self.blob_service_client.get_container_client(container_name)

    def upload_data(self, data, blob_name):
        blob_client = self.container_client.get_blob_client(blob_name)
        blob_client.upload_blob(data, overwrite=True)
        return blob_client.url
