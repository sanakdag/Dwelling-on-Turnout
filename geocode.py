import csv
from geopy import geocoders
from geopy.exc import GeocoderTimedOut
from geopy.geocoders import GoogleV3

geolocator = # use your API key
input = open('../DATA/B1.csv', 'r')
output = open('../DATA/coords.csv', 'a')
writer = csv.writer(output)
addr = ""


from geopy.extra.rate_limiter import RateLimiter
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)

prev = ""
prevlat = ""
prevlong = ""

for row in csv.reader(input):
    if row[43] == "" and row[0] != "":
        addr = row[11] + " " + row [13]
        addr = addr.title()
        addr = addr + " Brookline MA"
        print(addr)
        if prev != addr:
            prev = addr
            location = geolocator.geocode(addr, timeout=10)
            prevlat = location.latitude
            prevlong = location.longitude
        row[43] = prevlong
        row[44] = prevlat
        print((prevlat, prevlong))
        writer.writerow(row)

input.close()
output.close()
