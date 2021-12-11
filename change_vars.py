import xml.etree.ElementTree as ET
# %%

def main():
	file_name = 'Hercules DJ Inpulse 500 copy 2.djm'
	tree = ET.parse(file_name)
	root = tree.getroot()

	midi_map = root.find('midi-map')
	if midi_map is None:
		return

	for child in midi_map:
		attribs = child.attrib
		print(attribs['name'])
		name = attribs['name']
		if name.startswith('BEATJMP'):
			num = name[-3]
			deck = name[-1]

			if deck == 'A':
				attribs['action'] = beatjump_text(1, -1)

		# value = attribs['value']
		# value = '3'
		# for attrib in child.attrib:
			# print(attrib.)

	file_name_2 = 'Hercules DJ Inpulse 500 copy edited.djm'
	tree.write(file_name_2)


def beatjump_text(channel, beats):
	return f'chann={channel}  action=skip_beat value="{beats}"'


if __name__ == '__main__':
	main()