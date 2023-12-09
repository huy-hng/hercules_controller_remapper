import xml.etree.ElementTree as ET


def find_child_by_name(element, name):
	for child in element:
		if child.attrib['name'] == name:
			return child
	return None

def replace_element(parent, custom_element_file):
	custom_element = ET.parse(custom_element_file)
	custom_element = custom_element.getroot()

	for child in custom_element:
		custom_child_name = child.attrib['name']
		og_child = find_child_by_name(parent, custom_child_name)

		if og_child is not None:
			parent.remove(og_child)

		parent.append(child)

def main():
	file_name = './midi_templates/Hercules DJ Inpulse 500_31.djm'
	tree = ET.parse(file_name)
	root = tree.getroot()

	midi_map = root.find('midi-map')
	midi_device = root.find('midi-device')
	if midi_map is None or midi_device is None:
		print('sth wrong fam')
		return
	# root.remove(midi_map)

	# default_midi_map = ET.parse('./custom/default_map.html')
	# root.append(default_midi_map.getroot())

	replace_element(midi_map, './custom/custom_map.xml')
	replace_element(midi_device, './custom/custom_control.xml')

	tree.write('Hercules DJ Inpulse 500 - Custom.djm')

if __name__ == '__main__':
	main()
