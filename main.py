import xml.etree.ElementTree as ET
from pathlib import Path

VERSION = '31'

PROJECT_PATH = Path.cwd()
CMP_PATH = PROJECT_PATH / 'midi_components' / f'v{VERSION}'
CUSTOM_PATH = PROJECT_PATH / 'custom'

# INPUT_FILE = './midi_templates/Hercules DJ Inpulse 500_31.djm'
# OUTPUT_FILE = 'Hercules DJ Inpulse 500 - Custom.djm'

INPUT_FILE = CMP_PATH / 'template.xml'
OUTPUT_FILE = 'test.djm'


def find_child_by_name(element, name):
    for child in element:
        if child.attrib['name'] == name:
            return child
    return None


# not needed for now
midi_info = {
    'hw-in-mix-off': 'F000014E1C02017F000000000000F7',
    'hw-in-mix-on': 'F000014E1C02017F000001000000F7',
    'sysex': 'F07E7F060200014E02001C0001000000F7',
    'version': '31',
    'name': 'DJControl Inpulse 500',
    'map-name': 'Hercules Inpulse 500 - Custom Mapping',
    'description': 'Hercules Inpulse 500 Custom Mapping'
}


def add_element(root: ET.Element, filename):
    element = ET.parse(filename).getroot()
    root.append(element)


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

    add_element(root, CMP_PATH / 'device.xml')
    add_element(root, CMP_PATH / 'map.xml')
    add_element(root, CMP_PATH / 'picture.xml')

    midi_map = root.find('midi-map')
    midi_device = root.find('midi-device')

    replace_element(midi_map, CUSTOM_PATH / 'map.xml')
    replace_element(midi_device, CUSTOM_PATH / 'control.xml')

    tree.write(OUTPUT_FILE)


if __name__ == '__main__':
    main()
