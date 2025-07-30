import os
import uuid
import random

# Define the food items to be generated
food_items = [
    {"name": "Avocado Toast", "price": "6.50", "description": "Whole grain toast topped with smashed avocado and a sprinkle of salt", "calories": "350"},
    {"name": "Breakfast Burrito", "price": "9.50", "description": "A flour tortilla filled with scrambled eggs, cheese, and salsa", "calories": "800"},
    {"name": "Granola Bowl", "price": "5.50", "description": "Homemade granola served with yogurt and honey", "calories": "600"},
    {"name": "Eggs Benedict", "price": "10.95", "description": "Poached eggs on English muffin with ham and hollandaise sauce", "calories": "700"},
    {"name": "Chia Pudding", "price": "4.50", "description": "Chia seeds soaked in almond milk, topped with berries", "calories": "250"},
    {"name": "French Toast", "price": "6.95", "description": "Thick slices of bread dipped in egg and grilled, served with syrup", "calories": "750"},
    {"name": "Smoked Salmon Bagel", "price": "8.50", "description": "Bagel topped with cream cheese, smoked salmon, and capers", "calories": "500"},
    {"name": "Peanut Butter Banana Toast", "price": "5.00", "description": "Whole grain toast topped with peanut butter and banana slices", "calories": "400"},
    {"name": "Breakfast Sandwich", "price": "7.50", "description": "Egg, cheese, and sausage on a toasted bagel", "calories": "600"},
    {"name": "Quinoa Bowl", "price": "8.00", "description": "Quinoa topped with avocado, cherry tomatoes, and a poached egg", "calories": "450"},
]

# Create a directory to store the XML files
os.makedirs("breakfast_menus", exist_ok=True)

# Generate XML files
for i in range(1, 101):
    item = random.choice(food_items)  # Randomly select a food item
    file_name = f"breakfast_menus/food_item_{i}.xml"
    with open(file_name, 'w') as file:
        file.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        file.write('<food>\n')
        file.write(f'    <guid>{uuid.uuid4()}</guid>\n')  # Unique identifier
        file.write(f'    <name>{item["name"]}</name>\n')
        file.write(f'    <price>{item["price"]}</price>\n')
        file.write(f'    <description>{item["description"]}</description>\n')
        file.write(f'    <calories>{item["calories"]}</calories>\n')
        file.write('</food>\n')

print("100 XML files created successfully!")
