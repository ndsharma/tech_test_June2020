#!/usr/bin/env bash
# debug
#set -x

echo "Check the number of bikes at the given Bike Stand."
read -p "Enter the name of the Bike point: " BikePoint_Name
echo "Please Wait while I am checking bikes available at $BikePoint_Name"
BikePoint_ID=$(curl -X GET -G --data-urlencode "query=$BikePoint_Name" 'https://api.tfl.gov.uk/BikePoint/search/?' 2>/dev/null | cut -d ',' -f3 | cut -d '"' -f4 )
BikePoint_Count=$(curl -X GET "https://api.tfl.gov.uk/BikePoint/${BikePoint_ID}/" 2>/dev/null | awk -F "NbBikes" '{print $2}' | cut -d ',' -f3 | cut -d '"' -f4 )
echo "Currently there are $BikePoint_Count bikes available at $BikePoint_Name"
