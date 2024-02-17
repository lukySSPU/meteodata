import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
# Načtení dat z Excel souboru


# Definice třídy pro analýzu teplot
class TemperatureAnalytics:
    def __init__(self, data):
        self.data = data

    def get_available_years(self):
        return self.data['rok'].unique()

    def get_average_temperature(self, year):
        yearly_data = self.data[self.data['rok'] == year]
        return yearly_data['T-AVG'].mean()

    def get_max_temperature(self, year):
        yearly_data = self.data[self.data['rok'] == year]
        max_temp = yearly_data['TMA'].max()
        date_of_max_temp = yearly_data[yearly_data['TMA'] == max_temp][['rok', 'měsíc', 'den']].iloc[0]
        return max_temp, date_of_max_temp

    def get_min_temperature(self, year):
        yearly_data = self.data[self.data['rok'] == year]
        min_temp = yearly_data['TMI'].min()
        date_of_min_temp = yearly_data[yearly_data['TMI'] == min_temp][['rok', 'měsíc', 'den']].iloc[0]
        return min_temp, date_of_min_temp

    def get_monthly_averages(self, year):
        yearly_data = self.data[self.data['rok'] == year]
        return yearly_data.groupby('měsíc')['T-AVG'].mean()

    def analyze_temperature_trends(self, start_year, end_year):
        trend_data = self.data[(self.data['rok'] >= start_year) & (self.data['rok'] <= end_year)]
        annual_average_temperatures = trend_data.groupby('rok')['T-AVG'].mean()
        return annual_average_temperatures

    def plot_annual_temperature_averages(self, start_year, end_year):
        filtered_data = self.data[(self.data['rok'] >= start_year) & (self.data['rok'] <= end_year)]
        annual_average_temperatures = filtered_data.groupby('rok')['T-AVG'].mean()
        plt.figure(figsize=(10,0))
        plt.plot(annual_average_temperatures.index,annual_average_temperatures.values,marker='o',linestyle='-',color='r')
        plt.title(f'Průměrné roční teploty mezi lety {start_year} a {end_year}')
        plt.xlabel('Rok')
        plt.ylabel('Průměrná teplota (°C)')
        plt.grid(True)
        plt.show()

    def input_year_value(self):
        available_years = self.get_available_years()
        while True:
            user_input_year = int(input("Zadejte rok mezi 1775 - 2022: "))
            if user_input_year in available_years:
                break
        return user_input_year
    
    def input_month_value(self):
        while True:
            user_input_month = int(input("Zadejte měsíc: "))
            if user_input_month < 12 or user_input_month > 1:
                break
        return user_input_month
    
    def get_all_monthly_statistics(self, year):
        yearly_data = self.data[self.data['rok'] == year]
        monthly_statistics = []

        for month in range(1, 13):
            monthly_data = yearly_data[yearly_data['měsíc'] == month]
            average_temp = monthly_data['T-AVG'].mean()
            max_temp = monthly_data['TMA'].max()
            date_of_max_temp = monthly_data[monthly_data['TMA'] == max_temp][['rok', 'měsíc', 'den']].iloc[0]
            min_temp = monthly_data['TMI'].min()
            date_of_min_temp = monthly_data[monthly_data['TMI'] == min_temp][['rok', 'měsíc', 'den']].iloc[0]

            monthly_statistics.append({
                'měsíc': month,
                'průměrná teplota': average_temp,
                'maximální teplota': max_temp,
                'datum max teploty': f"{date_of_max_temp['den']}.{date_of_max_temp['měsíc']}.{date_of_max_temp['rok']}",
                'minimální teplota': min_temp,
                'datum min teploty': f"{date_of_min_temp['den']}.{date_of_min_temp['měsíc']}.{date_of_min_temp['rok']}",
            })

        return monthly_statistics
    
    def get_all_monthly_statistics(self, year):
        monthly_averages = self.get_monthly_averages(year)
        monthly_statistics = []

        for month, average_temp in monthly_averages.items():
            monthly_data = self.data[(self.data['rok'] == year) & (self.data['měsíc'] == month)]
            if not monthly_data.empty:
                max_temp = monthly_data['TMA'].max()
                date_of_max_temp = monthly_data.loc[monthly_data['TMA'].idxmax()][['rok', 'měsíc', 'den']]
                min_temp = monthly_data['TMI'].min()
                date_of_min_temp = monthly_data.loc[monthly_data['TMI'].idxmin()][['rok', 'měsíc', 'den']]

                monthly_statistics.append({
                    'měsíc': month,
                    'průměrná teplota': average_temp,
                    'maximální teplota': max_temp,
                    'datum max teploty': f"{date_of_max_temp['den']}.{date_of_max_temp['měsíc']}.{date_of_max_temp['rok']}",
                    'minimální teplota': min_temp,
                    'datum min teploty': f"{date_of_min_temp['den']}.{date_of_min_temp['měsíc']}.{date_of_min_temp['rok']}",
                })
        
        return monthly_statistics