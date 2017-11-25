#!/usr/local/bin/python
# coding: latin-1-
import io
import urllib2
import json
import unicodedata
from FileWorker import FileWorker




fileworker = FileWorker()

filename = './outputs/buildings_pois.json'
output_fn='./outputs/buildings_scores.csv'

output=open(output_fn,'w')
infoEdificios = fileworker.readJSON(filename)


data = infoEdificios['data']
coordenadas = {}

for idEdificio in data:
  d={}
  dict_venues=data[idEdificio]['venues']
  num_venues=len(list(dict_venues.keys()))
  total_checkins=0
  for id_venue in dict_venues:
    total_checkins+=dict_venues[id_venue]['checkins']
  for id_venue in dict_venues:
    d[id_venue]=dict_venues[id_venue]['checkins']/total_checkins

  scoreList=list(dict_venues.values())
  score=
  line=data[idEdificio]⁺","+num_venues+","+score
  output.write(line)

