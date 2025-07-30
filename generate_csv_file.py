import os
import csv
import xml.etree.ElementTree as ET

# Create a list to hold the food item data
food_items = []

# Directory containing the XML files
directory = 'breakfast_menus'

# Read each XML file and extract the data
for filename in os.listdir(directory):
    if filename.endswith('.xml'):
        file_path = os.path.join(directory, filename)
        tree = ET.parse(file_path)
        root = tree.getroot()
        
        # Extract data from XML
        guid = root.find('guid').text
        name = root.find('name').text
        price = root.find('price').text
        description = root.find('description').text
        calories = root.find('calories').text
        
        # Append the data to the list
        food_items.append({
            "guid": guid,
            "name": name,
            "price": price,
            "description": description,
            "calories": calories
        })

# Create a CSV file
with open('breakfast_menu.csv', mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["guid", "name", "price", "description", "calories"])
    writer.writeheader()
    for item in food_items:
        writer.writerow(item)

print("CSV file created successfully!")
