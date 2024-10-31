import requests
import json

# Define the order data
ordered_pizzas = {
      "orderId": 4,
      "status": "Not started",
      "pizzas": {
         "Margherita": 2,
         "4 Formaggi": 1
      }
   }

# Define the URL of your Flask app's order endpoint
url = "http://localhost:5001/order"  # Adjust the URL if needed

# print("Hello im good")
# Send the POST request with JSON data
try:
   response = requests.post(url, json=ordered_pizzas)
   # Check if the request was successful
   if response.status_code == 302:  # 302 indicates a redirection (successful submission)
      print("Order submitted successfully! Redirected to:", response.headers['Location'])
   elif response.ok:
      print("Order submitted successfully, but no redirect:", response.text)
   else:
      print("Failed to submit order. Status code:", response.status_code)
      print("Response:", response.text)

except Exception as e:
   print("Error occurred while submitting the order:", e)
