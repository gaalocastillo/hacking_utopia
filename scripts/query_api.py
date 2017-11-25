#from pymongo import MongoClient
import requests
from requests.auth import HTTPBasicAuth
import json


'''
============== 1 =============
Obtener numero de Workplaces
    fn = count
    of = desk
    *timeFilter.start
    *timeFilter.end
    *by = floor,attributeType         Number of workspaces by floor
    *by = building                    Number of workspaces by building

REVISAR TODAS EN API.HTML

'''


s = requests.session()

HOST = "https://hack.lct.ee/api/v1/"

# GET
r = s.post("https://hack.lct.ee/dologin", data={'username': "galo.castillo", 'password': 'galoxD14123456789'})

FN = "sum" #count, sum, max, min, avg
OF = "desks.occupied" #desks, desks.occupied, desks.workhourOccupied
BY = "hour"

buildings = [6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35]
'''
for building in buildings:
	BUILDING = str(building) #Id of specific building
	FLOOR = "" #Id of specific floor
	ATTRIBUTE_NAME = "" # depends on location
	ATTRIBUTE_ID = "" # depends on location

	START = "2017-01-01T00:00:00%2B02:00" # starting time window
	END = "2017-12-31T23:59:59%2B02:00" # ending time window

	PARAM_NAMES = ["fn", "of", "by", "locationFilter.building", "locationFilter.floor", "locationFilter.attribute.", "timeFilter.start", "timeFilter.end"]
	PARAMS = [FN, OF, BY, BUILDING, FLOOR, ATTRIBUTE_NAME, START, END]

	# Query Builder

	query_builder = "?"
	for i, param in enumerate(PARAMS):
	    if param == "":
	        continue
	    if PARAM_NAMES[i] == "locationFilter.attribute.":
	        query_builder += "locationFilter.attribute." + ATTRIBUTE_NAME + "=" + ATTRIBUTE_ID
	        continue
	    query_builder += PARAM_NAMES[i] + "=" + param

	    if i != len(PARAMS) -1:
	        query_builder += "&"


	print query_builder
	print HOST + "stats" + query_builder
	response = s.get(HOST + "stats" + query_builder)
	print response
	if str(response.status_code).startswith("2"):
		response = response.json()
		print response
		print len(response)
		with open('../outputs/%s_occupied_day.json' %BUILDING, 'w') as fp:
		    json.dump(response, fp)
	else:
		print ("Something went wrong! Error %d" % response.status_code)
'''
BUILDING = "32" #Id of specific building
FLOOR = "" #Id of specific floor
ATTRIBUTE_NAME = "" # depends on location
ATTRIBUTE_ID = "" # depends on location

START = "2017-01-01T00:00:00%2B02:00" # starting time window
END = "2017-12-31T23:59:59%2B02:00" # ending time window

PARAM_NAMES = ["fn", "of", "by", "locationFilter.building", "locationFilter.floor", "locationFilter.attribute.", "timeFilter.start", "timeFilter.end"]
PARAMS = [FN, OF, BY, BUILDING, FLOOR, ATTRIBUTE_NAME, START, END]

# Query Builder

query_builder = "?"
for i, param in enumerate(PARAMS):
    if param == "":
        continue
    if PARAM_NAMES[i] == "locationFilter.attribute.":
        query_builder += "locationFilter.attribute." + ATTRIBUTE_NAME + "=" + ATTRIBUTE_ID
        continue
    query_builder += PARAM_NAMES[i] + "=" + param

    if i != len(PARAMS) -1:
        query_builder += "&"


print query_builder
print HOST + "stats" + query_builder
response = s.get(HOST + "stats" + query_builder)
print response
if str(response.status_code).startswith("2"):
	response = response.json()
	print response
	print len(response)
	with open('../outputs/%s_occupied_day.json' %BUILDING, 'w') as fp:
	    json.dump(response, fp)
else:
	print ("Something went wrong! Error %d" % response.status_code)