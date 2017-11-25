from FileWorker import FileWorker

def getCity(address):
	city = address.strip().split(' ')




json_filename = '../data/data.json'
worker = FileWorker()

floors_amount = 0
locations_amount = 0
buildings = worker.readJSON(json_filename)['buildings']
#print len(buildings)

ids = set()
for building in buildings:
	if building['id'] == 11:
		for floor in building['floors']:
			for location in floor['locations']:
				ids.add(location['id'])
print len(ids)