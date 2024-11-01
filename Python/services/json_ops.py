import json

# Read data from a JSON file and return it as a Python object.
def read_from_json(fileName):
   try:
      print(f"Attempting to open file: {fileName}")
      with open(fileName, 'r', encoding='utf-8') as file:
         data = json.load(file)
      return data
   except FileNotFoundError:
      print(f"Error: The file '{fileName}' does not exist.")
      return None
   except json.JSONDecodeError:
      print(f"Error: The file '{fileName}' is not a valid JSON.")
      return None
   except Exception as e:
      print(f"An unexpected error occurred: {e}")
      return None

# Write data to a JSON file.
def write_to_json(fileName, data):
   try:
      with open(fileName, 'w') as file:
         json.dump(data, file, indent = 3)
      print(f"Successfully wrote to '{fileName}'.")
   except Exception as e:
      print(f"An error occurred while writing to the file: {e}")


# Append a new entry to a JSON file.
def append_to_json(fileName, newEntry):
   try:
      # Read existing data
      data = read_from_json(fileName)
      
      if data is None:
         write_to_json(fileName, newEntry)
      else:
         # Append the new entry
         data.append(newEntry)
         write_to_json(fileName, data)
      
   except Exception as e:
      print(f"An error occurred while appending to the file: {e}")

def save_order(order):
   orders = read_from_json("data/orders.json")
   orderId = 0
   if orders:
      last_order = orders[-1]
      orderId = last_order["orderId"] + 1

   order["orderId"] = orderId
   append_to_json("data/orders.json", order)

   return orderId