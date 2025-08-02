import xml.etree.ElementTree as ET
import pandas as pd


xml_file = 'data.xml'  # Path to your XML file
tree = ET.parse(xml_file)
root = tree.getroot()


data = []

for entry in root.findall('entry'):
    entry_data = {}


    # Extract time, value, and description
#    for child in entry:
#        if child.tag == 'location':
#            # Process location separately
#            for loc_child in child:
#                loc_tag = loc_child.tag
#                loc_text = loc_child.text.strip() if loc_child.text else None
#                entry_data[loc_tag] = loc_text
#        elif child.tag == 'measurements':
#            # Process measurements
#            for measurement in child.findall('measurement'):
#                measurement_type = measurement.find('type').text.strip()
#                measurement_value = measurement.find('value').text.strip()
#                entry_data[f'measurement_{measurement_type}'] = measurement_value
#       else:
#           entry_data[child.tag] = child.text.strip() if child.text else None
#
#     data.append(entry_data)


df = pd.DataFrame(data)


print(df)


THIS ONE:

for entry in root.findall('entry'):
    entry_data = {}
    
    # Extract time, value, and description
    entry_data['time'] = entry.find('time').text.strip() if entry.find('time') is not None else None
    entry_data['value'] = entry.find('value').text.strip() if entry.find('value') is not None else None
    entry_data['description'] = entry.find('description').text.strip() if entry.find('description') is not None else None
    
    # Extract location data
    location = entry.find('location')
    if location is not None:
        entry_data['location_city'] = location.find('city').text.strip() if location.find('city') is not None else None
        entry_data['location_country'] = location.find('country').text.strip() if location.find('country') is not None else None
    
    # Extract measurements
    measurements = entry.find('measurements')
    if measurements is not None:
        for measurement in measurements.findall('measurement'):
            measurement_type = measurement.find('type').text.strip() if measurement.find('type') is not None else None
            measurement_value = measurement.find('value').text.strip() if measurement.find('value') is not None else None
            if measurement_type:
                entry_data[f'measurement_{measurement_type}'] = measurement_value
    
    data.append(entry_data)
