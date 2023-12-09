# %%
import xml.etree.ElementTree as ET
# %%

def main():
	# def get_tree(path)
	file_name = './midi_files/Hercules DJ Inpulse 500 copy 2.djm'
	tree = ET.parse(file_name)
	root = tree.getroot()

	midi_map = root.find('midi-map')
	if midi_map is None:
		return


	for child in midi_map:
		attribs = child.attrib
		# print(attribs['name'])
		name = attribs['name']
		if name.startswith('BEATJMP'):
			num = name[-3]
			deck = name[-1]
			
			change_value_in_action_attrib(child, 'value', '"-"')

			# if deck == 'A':
			# 	attribs['action'] = beatjump_text(1, -12)

		# value = attribs['value']
		# value = '3'
		# for attrib in child.attrib:
			# print(attrib.)

	file_name_2 = 'Test.djm'
	# print(midi_map[0].attrib)
	tree.write('./midi_files/' + file_name_2)


def beatjump_text(channel, beats):
	return f'chann={channel}  action=skip_beat value="{beats}"'

def change_value_in_action_attrib(element: ET.Element, target_attrib: str, new_val: str):
	# print(id(element))
	attribs = element.attrib
	action_attribs = attribs['action'].split(' ')
	for i, attrib in enumerate(action_attribs):
		if attrib.startswith(target_attrib):
			attrib = attrib.split('=')
			attrib[1] = new_val
			attrib = '='.join(attrib)
			action_attribs[i] = attrib

	element.attrib['action'] = ' '.join(action_attribs)



def find_name(branch: ET.Element, name: str):
	for child in branch:
		attribs = child.attrib
		if name == attribs['name']:
			return child



if __name__ == '__main__':
	main()
