from flask import Flask, jsonify
import random

app = Flask(__name__)

# In-memory storage for processed data
data_storage = {}

# Mock data simulating external service (e.g., Shopify)
mock_data = {
    "order_id": 12345,
    "customer_name": "John Doe",
    "total_price": 99.99,
    "items": [
        {"product": "T-shirt", "quantity": 2, "price": 20.0},
        {"product": "Jeans", "quantity": 1, "price": 59.99},
    ],
    "order_status": "Pending"
}

# API Endpoint for Data Retrieval
@app.route('/fetch-data', methods=['GET'])
def fetch_data():
    # Simulate fetching data from an external service by returning mock data
    return jsonify(mock_data)

# Data Processing function
def process_data(data):
    # Simple processing: converting customer name to uppercase
    processed_data = data.copy()
    processed_data['customer_name'] = processed_data['customer_name'].upper()

    # Simulate summing the total price of items
    total_price = sum(item['price'] * item['quantity'] for item in processed_data['items'])
    processed_data['total_price'] = round(total_price, 2)

    # Store processed data in memory
    order_id = processed_data['order_id']
    data_storage[order_id] = processed_data

    return processed_data

# API Endpoint to process and store data
@app.route('/process-data', methods=['GET'])
def process_and_store_data():
    data = mock_data  # In a real application, this would be fetched from an external service
    processed_data = process_data(data)
    return jsonify(processed_data)

# API Endpoint for Retrieving Processed Data
@app.route('/get-processed-data', methods=['GET'])
def get_processed_data():
    return jsonify(data_storage)

if __name__ == '__main__':
    app.run(debug=True)
