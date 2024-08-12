# Flask Data Retrieval and Processing System

This Flask application simulates a simplified version of a data retrieval and processing system. It includes the following features:

1. **API Endpoint for Data Retrieval**: 
   - `GET /fetch-data`: Simulates fetching data from an external service and returns mock data.

2. **Data Processing**: 
   - The application processes fetched data by converting the customer's name to uppercase and summing the total price of items.

3. **Data Storage**: 
   - The processed data is stored temporarily in in-memory storage (a Python dictionary).

4. **API Endpoint for Processed Data Retrieval**: 
   - `GET /get-processed-data`: Returns the processed data stored in memory.

## Getting Started

### Prerequisites

- Python 3.x
- Flask

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Rad-007/catalys.git
   cd flask_app
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

1. Start the Flask application:

   ```bash
   flask run
   ```

2. The application will run on `http://127.0.0.1:5000/`.

### API Endpoints

- **Fetch Data**:
  - URL: `/fetch-data`
  - Method: `GET`
  - Description: Simulates fetching data from an external service.

- **Get Processed Data**:
  - URL: `/get-processed-data`