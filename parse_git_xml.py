import xml.etree.ElementTree as ET
import pandas as pd
import numpy as np

xml_file = "git_example.xml"

tree = ET.parse(xml_file)

root = tree.getroot()

all_elements = list(root.iter())


data_records = []

for element in all_elements:
    record = {
        'tag':  element.tag,
        'text':  element.text.strip() if element.text else None,
        'attributes':  element.attrib
        }
    data_records.append(record)

df = pd.DataFrame(data_records)

df_filtered_on_brand = df.query("tag == 'brand'")

count = 0
for value in df_filtered_on_brand['text'].values:
    if value == 'Titleist Golf':
        count += 1
print(f"Number of instances of 'Titleist Golf':  {count}")


count = 0
for value in df_filtered_on_brand['text'].values:
    if value == 'Odyssey Golf':
        count += 1
print(f"Number of instances of 'Odyssey Golf':  {count}")

count = 0
for value in df_filtered_on_brand['text'].values:
    if value == 'TaylorMade Golf':
        count += 1
print(f"Number of instances of 'TaylorMade Golf':  {count}")



count = 0
for value in df_filtered_on_brand['text'].values:
    if value == 'Cobra Golf':
        count += 1
print(f"Number of instances of 'Cobra Golf' {count}")


#if __name__ == "__main__":


