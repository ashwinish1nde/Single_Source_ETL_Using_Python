# Single Source ETL using Python

## Overview
Simple Python-based ETL (Extract, Transform, Load) solution for transferring data from JSON files to PostgreSQL databases.

## Features
- Extract data from JSON files.
- Transform data as needed.
- Load data into PostgreSQL databases.
  
![ETL Process](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*ypCpRfnMC-8mugYv.jpg)

## File Structure
- `main_ETL.py`: Main script to initiate the ETL process.
- `Utilities/`: Directory containing helper scripts and utilities.
  - `helper_psql.py`: Script for PostgreSQL database operations.
  - `get_data.py`: Script for extracting data from JSON files.
- `data/`: Directory for storing input JSON files.
- `requirements.txt`: File listing all dependencies required for the project.

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/ashwinish1nde/Single_Source_ETL_Using_Python.git
   ```
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
1. Ensure you have a PostgreSQL database set up.
2. Modify configuration settings in `main_ETL.py` and `Utilities/helper_psql.py` to match your database credentials and JSON file paths.
3. Run the ETL process:
   ```
   python main_ETL.py
   ```


