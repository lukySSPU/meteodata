# Meteodata Analysis

## Overview

Meteodata Analysis is a Python project designed for temperature analytics based on historical weather data. The project includes functionalities to analyze yearly, monthly, and specific monthly temperature statistics, visualize temperature trends, and detect anomalies.

## Requirements

- Python 3.x
- pandas
- matplotlib
- numpy

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/meteodata.git
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Project Structure

- **main.py**: Main script to execute the temperature analysis and user interactions.
- **temperature.py**: Module containing the `TemperatureAnalytics` class for temperature-related computations.
- **data/klementinum.xlsx**: Sample historical weather data in Excel format.
- **month_names.py**: Module with a dictionary mapping month numbers to month names.

## Usage

1. Run the main script:

   ```bash
   python main.py
   ```

2. Choose an option:
   - 1: Yearly temperature statistics
   - 2: Monthly temperature statistics
   - 3: Monthly statistics for a specific month in a year
   - 4: Analyze temperature trends
   - 5: Analyze seasonal changes
   - 6: Detect temperature anomalies
   - 7: Plot average annual temperatures
   - 8: Plot daily temperature trends
   - 9: Plot minimum and maximum temperatures for a specific day

3. Follow the prompts and input necessary information.