import xml.etree.ElementTree as ET

def create_nested_xml(filename, depth, num_children):
    """
    Generates a deeply nested XML file.

    Args:
        filename (str): The name of the XML file to create.
        depth (int): The maximum nesting depth.
        num_children (int): The number of children each element can have.
    """
    root = ET.Element("root")
    current_element = root

    for i in range(depth):
        new_parent = ET.SubElement(current_element, f"level_{i}")
        new_parent.set("id", str(i))
        new_parent.text = f"Data at level {i}"

        for j in range(num_children):
            child = ET.SubElement(new_parent, f"child_{j}")
            child.set("child_id", str(j))
            child.text = f"Child data {j} at level {i}"

        current_element = new_parent

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True, pretty_print=True)

# Generate 10 deeply nested XML files
for i in range(1, 11):
    filename = f"nested_xml_{i}.xml"
    create_nested_xml(filename, depth=10 + i, num_children=2) # Increasing depth for each file
    print(f"Generated {filename}")
