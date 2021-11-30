
# %%
import xml.etree.ElementTree as ET

file_name = './midi_files/Hercules DJ Inpulse 500.djm'
tree = ET.parse(file_name)
root = tree.getroot()

data = {}

for child in root.find('midi-device'):
	name = child.attrib['name']
	data[name] = []
	# for child_ in child:

for child in root.find('midi-map'):
	name = child.attrib['name']
	if name in data:
		data[name] = data[name].update(child.attrib)
	else:
		data[name] = child.attrib

print(data)
# with open('data.csv', 'w') as f:
