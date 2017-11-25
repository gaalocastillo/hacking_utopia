from pymongo import MongoClient
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

#  ======== VARIABLES A CAMBIAR =========

FN = "count" #count, sum, max, min, avg
OF = "desks" #desks, desks.occupied, desks.workhourOccupied
BY = ""

BUILDING = "32" #Id of specific building
FLOOR = "" #Id of specific floor
ATTRIBUTE_NAME = "" # depends on location
ATTRIBUTE_ID = "" # depends on location

START = "2017-07-01T00:00:00%2B02:00" # starting time window
END = "2017-12-31T23:59:59%2B02:00" # ending time window

# ==================================== #


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
response = response.json()  #objeto json
print response
print len(response)