def normalize_and_convert_to_float(value):
    # Remove spaces (thousand separators)
    value = value.replace(' ', '')
    # Replace comma with dot (decimal separators)
    value = value.replace(',', '.')
    # Convert to float
    return float(value)

# Assuming json_data is your JSON data as a dictionary
json_data = {
    "key1": "1 000,50",
    "key2": "2 500,00",
    "key3": "3 000.00"  # Assuming some values might already be in correct format
}

# Loop through the dictionary and convert all values
for key in json_data:
    json_data[key] = normalize_and_convert_to_float(json_data[key])

print(json_data)
