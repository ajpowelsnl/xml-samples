import pandas as pd
import xml.etree.ElementTree as ET

def parse_xml_to_dataframe(xml_file):
    # Parse the XML file
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Initialize a list to hold the data
    data = []

    # Recursive function to extract data from XML elements
    def extract_data(entry):
        entry_data = {}
        for child in entry:
            if len(child) > 0:  # If the child has its own children
                # Recursively extract data from the child
                child_data = extract_data(child)
                entry_data[child.tag] = child_data
            else:
                entry_data[child.tag] = child.text  # Extract tag and text
        return entry_data

    # Iterate through the XML structure
    # 'entry' refers to each individual XML element that matches the specified tag
    try:
        for entry in root.findall('.//entry'):  # Replace 'entry' with your actual entry tag
            # Extract data from the current entry element
            entry_data = extract_data(entry)
            data.append(entry_data)
    except Exception as e:
        print(f"Error while processing entries: {e}")

    # Create a DataFrame
    df = pd.json_normalize(data)  # Use json_normalize to flatten nested structures
    return df

# Example usage
xml_file_path = 'path/to/your/file.xml'  # Replace with your XML file path
df = parse_xml_to_dataframe(xml_file_path)

# Display the DataFrame
print(df)
