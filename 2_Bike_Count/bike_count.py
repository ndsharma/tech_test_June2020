# Author - Nitin Dutt Sharma
# Date - 30/05/2020
# Version - 1.0
# importing libraries
import requests, json
print ("Checking the number of bikes available at Bank of England Museum, Bank")
print ("Hope you are having a Great Day.\n"
"Please Wait as this may take some time")
bikepoint = "Bank of England Museum, Bank"
URL = "https://api.tfl.gov.uk/BikePoint/"
URL_search = "https://api.tfl.gov.uk/BikePoint/Search?query={0}".format(bikepoint).replace(' ','%20')
response = requests.get(URL_search)
bikepoint_data = (response.json())
bikepoint_ID = (bikepoint_data[0]['id'])
URL = URL + bikepoint_ID
details = requests.get(URL)
bikepoint_details = (details.json())
additionalProperties = bikepoint_details['additionalProperties']
for items in additionalProperties:
    if items['key']=="NbBikes":
        bikes = items['value']

availability = f"Currently there are {bikes} available at {bikepoint}"
print(availability)
