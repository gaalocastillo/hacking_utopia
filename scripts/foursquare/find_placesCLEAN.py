#!/usr/local/bin/python
# coding: latin-1-
import io
import urllib2
import json, requests
import unicodedata
from FileWorker import FileWorker



listaClientIDs = ["0125VG400XXUPPTHKROUI4BJBAYBAS4T1QL0WC0IQPBDP0M2",
                  "4FM5TWUUR5DTFJWLMAVUFPPF003K5EOHWOTPHDHEQVSDLJYL",
                  "X1VEOVHXX4SEHF3U5F0VR41JTWGF4JCWFSTPY42ZB1W2D4IG",
                  "31EXRFXXKZHCTXWZPZSMHUWA2XAAW54EJOGCTACWT3REPKCI",
                  "QETSDZBFBT4BXYUPYS0K2NN1MJJ4MM1ZALNVYSFQ5AYRF0JO",
                  "ZYC444ZB3GAIWL1RZHNMVMT3PY5WCQJIGTHG3DQYOLO1RU1T",
                  "FCWMSURYUQRSQHAFK43BUWPL032XO1AUGNPA1PR4EDCGGVFR",
                  "YKKBKQXTNDOZ2UGSH5DK4RBOYKAO0VS5BWOFMM0GBCYMRL4K",
                  "P5OH4OJSWORALBTV55LXHFZZQZ05WJXBZEIKKYWG4LKIE4MI",
                  "NYKGI5XX4GMBITG4ULA5QU0AFQBBSDNWL5LIQENTUTZUGTGI",
                  "BEYSSUOCQIF2ZQGYX5OZGIL5SNHE25SMEPAWSEQB5XV5AEEW"]


listaClientSecrets = ["SED3ZC05NNINFXU5FB1FEMHIGRFRECRMUKB4AALUSXE4DJOF",
                      "MGNKASEZGGVGKJB5ZI4LQKCYON534XSVY2LWCCT0FJTCNP10",
                      "NZ3CQ20XFCJ22LINI2INFKSV024YUUJ4DI4JABI3BQ04JCLO",
                      "FCH0HJGU50X04DQAPSDTQJZERK1KJQRBV5ZVB3DUR40QAUCD",
                      "B3Y2AK5XXXMNRBPNVDO40LZ20LBB0ZZXVTOQFOCMNLNABOML",
                      "ZJJQGQFZBEQJHUOCLQ1VGWOTDD55MDNXOERUKJBP0JQHVGWR",
                      "RA3DWJZJX2BTYCI1GDASLOHHEWBXD1YNYVV5JSFYZ1TJRR21",
                      "Z55UUPEPE1PNJHKAOTPFJ5DXS2FEYYTLKDIZYHLNUZ5BIOLN",
                      "N1F3CS5GXGGUNU2IWG33VBYIPN3KPMI3H1A144FNATVYVM5Q",
                      "H1QVKPKF13KGRMCICGZBKPW5EZG12QXHMW1LIKS1TWEBRMOV",
                      "I3HEXOZC2DXOKGHKWBB3WQVWHMKKOFMKJBYUCPIQDVSSDEEY"]

indice = 0

dictBase={}
fileworker = FileWorker()

#ABRO EL ARCHIVO CON LOS DATOS DE LOS EDIFICIOS
filename = '../../data/buildings.csv'

file=open(filename)
file.readline()
for line in file:
  datos=line.split(",")
  lat = datos[3]
  lng = datos[4]
  ciudad = datos[-1]
  id_edificio=datos[2]
  nombre_edificio=datos[1]
  lat_lng = lat + ',' + lng

  if lat_lng == '0,0':
    continue

  #limit representa la cantidad maxima de venues que se extraeran por coordenada
  limit = '50'

  #radius representa el radio maximo en metros de extraccion de venues cercanos por coordenada
  radius = "200"

  #fecha del dia actual
  v = "20171124"

  try:
    url = "https://api.foursquare.com/v2/venues/search?ll="+lat_lng+"&limit="+limit+"&radius="+radius+"&client_id="+listaClientIDs[indice%11]+"&client_secret="+listaClientSecrets[indice%11]+"&v="+v
    raw_json = urllib2.urlopen(url)
    data = json.load(raw_json)

  except:
    print "\n\n\tCAMBIO DE API KEYS\n\n"
    indice += 1
    url = "https://api.foursquare.com/v2/venues/search?ll=" + lat_lng + "&limit=" + limit + "&radius=" + radius + "&client_id=" + \
          listaClientIDs[indice%11] + "&client_secret=" + listaClientSecrets[indice%11] + "&v=" + v

    raw_json = urllib2.urlopen(url)
    data = json.load(raw_json)

  infoLugares={}
  if len(data["response"]["venues"]) > 0 :
    size=len(data["response"]["venues"])
    count=0
    type=""
    while(count<size):
    
      id_lugar=data["response"]["venues"][count]["id"]
      place = data["response"]["venues"][count]["name"]

      place = unicodedata.normalize('NFKD', place)

      
      if(len(data["response"]["venues"][count]["categories"])>0):
          type = data["response"]["venues"][count]["categories"][0]["name"]

      tips = data["response"]["venues"][count]['stats']['tipCount']
      tips = str(tips)

      checkins = data["response"]["venues"][count]['stats']['checkinsCount']
      checkins = str(checkins)
      latVenue=data["response"]['venues'][count]['location']['lat']
      lngVenue=data["response"]['venues'][count]['location']['lng']
      usersCount=data["response"]["venues"][count]['stats']['usersCount']
      lugar={"name":place,"lat":latVenue,"lng":lngVenue,"usersCount":usersCount,"tipCount":tips,"category":type, "checkins" : checkins}
      infoLugares[id_lugar]=lugar

      if (type != '' and place != ''):
          #print type + "\t" + place + '\t' + tips + '\t' + checkins
          print place
      count+=1


  #Writes in JSON
  filename = '../../outputs/buildings_pois.json'
  useful_data = {'code':nombre_edificio,'lat': lat, 'lng': lng, 'city': ciudad, 'venues': infoLugares}
  dictBase[id_edificio]=useful_data
  
d={}
d["data"]=dictBase
fileworker.writeJSON(filename, d)

