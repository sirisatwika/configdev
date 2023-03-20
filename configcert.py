import requests
import json
# Set the URL for the other EdgeX Foundry instance
url = 'http://localhost:59981/api/v2/device'
# Set the device registration parameters
device_name = "satwika_device"
device_description = "demo"
device_profile_name = "satwika_ubuntu"
device_service_name = "satwika_ubuntu_service"
device_labels = {"location": "loc"}
# Set the device registration payload
payload = {
    "name": "satwika_device",
    "description": "demo",
    "profileName": "satwika_ubuntu",
    "serviceName": "satwika_ubuntu_serice",
    "labels": "dps"
}
# Set the path to your device certificate and private key files

cert_path = "./device_cert.crt"
key_path = "./device_private.key"
# Send the device registration request using your device certificate and private key verify='./ca_cert.crt',
response = requests.post(url, data=json.dumps(payload), cert=(cert_path, key_path), verify='./ca_cert.crt')
# Print the response
print(response.text)
