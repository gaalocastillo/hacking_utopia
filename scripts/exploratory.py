from FileWorker import FileWorker
import matplotlib.pyplot as plt


def getCity(address):
	city = address.strip().split(' ')

def group_same_names(names, values):
	new_names = []
	new_values = []

	for name_index in range(len(names)):
		name = names[name_index]
		value = values[name_index]
		if name not in new_names:
			new_names.append(name)
			new_values.append(value)
		else:
			new_index = new_names.index(name)
			new_values[new_index] += value
	return new_names, new_values


def show_biggest(d, n):
	biggest_keys = []
	biggest_values = []
	for key, value in d.items():
		if len(biggest_values) >= n:
			minimo = min(biggest_values)
			pos_min = biggest_values.index(minimo)
			biggest_values.remove(minimo)
			biggest_keys.pop(pos_min)
		biggest_keys.append(key)
		biggest_values.append(value)
	for i in range(len(biggest_values)):
		print biggest_keys[i], biggest_values[i]
	return dict(zip(biggest_keys, biggest_values))



data_filename = '../data/data.json'
attributes_filename = '../data/location_attributes.json'
worker = FileWorker()

floors_amount = 0
locations_amount = 0
buildings = worker.readJSON(data_filename)['buildings']
attributes = worker.readJSON(attributes_filename)['locationAttributes']
#print len(buildings)

attributes_names = {}

for attribute in attributes:
	attributes_names[ attribute['id'] ] = attribute['typeName']
#print attributes_names

ids = set()
attirbutes_ids = {}
for building in buildings:
	if building['id'] == 12:
		for floor in building['floors']:
			for location in floor['locations']:
				for d in location['locationAttributes']:
					if d['id'] not in attirbutes_ids:
						attirbutes_ids[d['id']] = 1
					else:
						attirbutes_ids[ d['id'] ] += 1



dictionary = show_biggest(attirbutes_ids, 15)
id_labels = dictionary.keys()
values = dictionary.values()

name_labels = []
for id in id_labels:
	name_labels.append(attributes_names[id])

total_values_sum = sum(attirbutes_ids.values()) - sum(values)

if total_values_sum != 0:
	name_labels.append('Others')
	id_labels.append('Others')
	values.append(total_values_sum)

actual_name_labels, actual_values = group_same_names(name_labels, values)

fig1, ax1 = plt.subplots()
ax1.pie(actual_values, labels=actual_name_labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
ax1.set_title('Bern Engehalde 39\nLocation Types Distribution')
plt.show()



