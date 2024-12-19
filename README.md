# assessment-firmable

## Overview
This application scrapes the homepage of a given website and answers key questions about the company.

## Features
- **Industry**: Identifies the industry of the company.
- **Company Size**: Estimates the company size.
- **Location**: Determines the location if mentioned.

## Getting Started

### Prerequisites
- Python 3.11+
- Poetry

### Setup
1. Clone the repository:
   ```bash
   git clone git@github.com:swarajb1/assessment-firmable.git
   cd assessment-firmable
   ```

2. Install dependencies:
   ```bash
   poetry install
   ```

3. Run the application:
   ```bash
   poetry run python main.py
   ```

### Usage
1. Start the FastAPI server:
   ```bash
   poetry run uvicorn main:app --reload
   ```

2. Open your browser and navigate to `http://127.0.0.1:8000/docs` to access the Swagger UI for API documentation and testing.


### License
This project is licensed under the CC0 1.0 Universal License - see the [LICENSE](LICENSE) file for details.

