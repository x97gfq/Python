import json
import requests

#https://data.novascotia.ca/Health-and-Wellness/Hospitals/tmfr-3h8a
api_url = "https://data.novascotia.ca/resource/tmfr-3h8a.json"

hospitals = []

response = requests.get(api_url)
if response.status_code == 200:
    hospitals = json.loads(response.content.decode("utf-8"))
    if hospitals is not None:
        for hospital in hospitals:
            hospital_name = hospital.get("facility")
            print(hospital_name)
            address = hospital.get("address");
            print(address);
    else:
        print('no hospitals found')
else:
    print('[!] Request Failed')