import json
import requests

class CrimeInfo:
    def __init__(self,_year = 0, _incidents = 0, _rates = 0, _violations = ""):
        self.year = _year
        self.incidents = _incidents
        self.rates = _rates
        self.violations = _violations

#https://data.novascotia.ca/Crime-and-Justice/Crime-Statistics-Incidents-and-rates-by-offence-ca/daey-6b54
api_url = "https://data.novascotia.ca/resource/daey-6b54.json"
search_term = "Barrington"

#a new class to hold our data from the API
def get_data():
    response = requests.get(api_url)
    if response.status_code == 200:
        return json.loads(response.content.decode("utf-8"))
    else:
        return None

info = get_data()

crimeData = []

if info is not None:
    for item in info:
        if (item["geography"].find(search_term) != -1):
            #instantiate new objets and populate them
            yr = item["year"][:4]
            incidents = item["incidents"]
            rates = item["rates"]
            violations = item["violations"]
            crime = CrimeInfo(yr, incidents, rates, violations)
            #add the new object to the collection
            crimeData.append(crime)
else:
    print('[!] Request Failed')

#sort the data by year
crimeData.sort(key=lambda x: x.year, reverse=True)

#output the results
print("Results for " + search_term + ":")
for crime in crimeData:
    print(crime.year + ": incidents: " + crime.incidents + ", rates: " + crime.rates + " (" + crime.violations + ")")