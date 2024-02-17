from temperature import TemperatureAnalytics
import pandas as pd

data_path = 'data/klementinum.xlsx'
data_sheet_name = 'data'
temperature_data = pd.read_excel(data_path, sheet_name=data_sheet_name)
temperature_analytics = TemperatureAnalytics(temperature_data)

available_years = temperature_analytics.get_available_years()

while True:
    user_input_year = int(input("Zadejte rok mezi 1775 - 2022: "))
    if user_input_year in available_years:
        break

temperature_data = user_input_year

average_temp = temperature_analytics.get_average_temperature(temperature_data)
max_temp, date_of_max_temp = temperature_analytics.get_max_temperature(temperature_data)
min_temp, date_of_min_temp = temperature_analytics.get_min_temperature(temperature_data)

average_temp_formatted = f"{average_temp:.2f}"
max_temp_formatted = f"{max_temp:.2f}"
min_temp_formatted = f"{min_temp:.2f}"

print(f"Průměrná teplota v roce {user_input_year}: {average_temp_formatted}°C")
print(f"Maximální teplota v roce {user_input_year}: {max_temp_formatted}°C, datum: {date_of_max_temp['den']}.{date_of_max_temp['měsíc']}.{date_of_max_temp['rok']}")
print(f"Minimální teplota v roce {user_input_year}: {min_temp_formatted}°C, datum: {date_of_min_temp['den']}.{date_of_min_temp['měsíc']}.{date_of_min_temp['rok']}")