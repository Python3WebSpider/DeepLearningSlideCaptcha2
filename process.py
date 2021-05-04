import xmltodict
import json


def parse_xml(file):
    xml_str = open(file, encoding='utf-8').read()
    data = xmltodict.parse(xml_str)
    data = json.loads(json.dumps(data))
    annoatation = data.get('annotation')
    width = int(annoatation.get('size').get('width'))
    height = int(annoatation.get('size').get('height'))
    bndbox = annoatation.get('object').get('bndbox')
    box_xmin = int(bndbox.get('xmin'))
    box_xmax = int(bndbox.get('xmax'))
    box_ymin = int(bndbox.get('ymin'))
    box_ymax = int(bndbox.get('ymax'))
    box_width = (box_xmax - box_xmin) / width
    box_height = (box_ymax - box_ymin) / height
    return box_xmin / width, box_ymax / height, box_width / width, box_height / height
