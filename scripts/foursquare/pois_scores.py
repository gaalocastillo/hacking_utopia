#!/usr/local/bin/python
# coding: latin-1-

import json
from FileWorker import FileWorker




fileworker = FileWorker()

filename = './outputs/buildings_pois.json'
output_fn='./outputs/buildings_scores.csv'

output=open(output_fn,'w')
infoEdificios = fileworker.readJSON(filename)
output.write("id,num_venues,scores"+"\n")

data = infoEdificios['data']
coordenadas = {}

for idEdificio in data:
  d={}
  dict_venues=data[idEdificio]['venues']
  print(dict_venues)
  num_venues=len(list(dict_venues.keys()))
  total_checkins=0
  if(num_venues==0):
    continue
  for id_venue in dict_venues:
    total_checkins+=int(dict_venues[id_venue]['checkins'])
  print("TOTAL CHECKINS: "+str(total_checkins))
  for id_venue in dict_venues:
    print(dict_venues[id_venue]['checkins'])
    d[id_venue]=int(dict_venues[id_venue]['checkins'])/float(total_checkins)

  scoreList=list(d.values())
 
  #scoreList=scoreList.sort()
  print(scoreList)
  score=0
  
  if(num_venues%2==0):
    s1=scoreList[num_venues/2]
    s2=scoreList[(num_venues/2)+1]
    score=(s1+s2)/2
  else:
    score=scoreList[(num_venues+1)/2]
  print("ASDFasd")
  print(str(num_venues))
  print(str(score))
  line=idEdificio+","+str(num_venues)+","+str(score)
  print (line)
  output.write(line+"\n")

