import xml.etree.ElementTree as ET

MAP_FILE = './custom/custom_map.xml'
CONTROL_FILE =  './custom/custom_control.xml'

INPUT_FILE = './midi_templates/Hercules DJ Inpulse 500_31.djm'
OUTPUT_FILE = 'Hercules DJ Inpulse 500 - Custom.djm'

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
	file_name = INPUT_FILE
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

	replace_element(midi_map, MAP_FILE)
	replace_element(midi_device, CONTROL_FILE)

    tree.write(OUTPUT_FILE)

if __name__ == '__main__':
	main()
