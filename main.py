"""
DTU SMART LIBRARY API EXAMPLE

This example shows how to use the API to get data from a sensor.
"""

import requests

# ======================================================================
# Set your API key or token here
API_KEY = "YOUR API KEY HERE"
# ======================================================================

# Set the headers
headers = {"Authentication": f"{API_KEY}" }
url = "https://dtusmartlib.azurewebsites.net/api/AirWits/GetAllDataFromSensor/C45899"


# Make the request
response = requests.get(url, headers=headers)

# Handle the response
if response.status_code == 200:
    print(response.json())
else:
    print(f"Failed with status code: {response.status_code}")
    print(response.text)