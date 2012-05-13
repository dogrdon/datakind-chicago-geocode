#this is a python file that geocodes the IVDRS addresses to a latitude and longitude
#all thanks to Joe Germuska

from geopy import geocoders 

import csv

g = geocoders.Google()

with open('./Data/Chicago-Only_Illinois_Violent_Death_Reporting_System_Data_Randomized.csv') as f:
	r = csv.reader(f)
	w = csv.writer(open('./Data/Chicago-Only_Illinois_Violent_Death_Reporting_System_Data_Randomized_with_latlong.csv', 'w'))
	header = r.next()
	header.extend(['lat', 'long'])
	w.writerow(header)

	for row in r:
		# do geocoding...
		results = g.geocode(row[3], exactly_one=False)
		first = results.next()
		if first:	
			place, (lat, lng) = results[0]
				
			row.extend([str(lat), str(lng)])
			w.writerow(row)
		else:
			print "Sorry, no geocodes for you!", row[3]
