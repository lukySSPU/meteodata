from temperature import TemperatureAnalytics
import pandas as pd
from month_names import month_names

data_path = 'data/klementinum.xlsx'
data_sheet_name = 'data'
temperature_data = pd.read_excel(data_path, sheet_name=data_sheet_name)
temperature_analytics = TemperatureAnalytics(temperature_data)

print("Vyberte možnost:")
print("1. Průměrné, max a min teploty v roce")
print("2. Průměrné, max a min teploty všech měsíců v roce")
print("3. Průměrné, max a min teploty v zadaném měsíci v roce")
print("4. Analyzovat teplotní trendy")
print("5. Analyzovat sezónní změny")
print("6. Detekovat teplotní anomálie")
print("7. Vykreslit průměrné roční teploty")
print("8. Vykreslit denní teplotní trendy")
print("9. Vykreslit minimální a maximální teploty pro konkrétní den")


option = int(input("Zadejte číslo možnosti: "))

if option == 1:
    
    user_input_year = temperature_analytics.input_year_value()

    average_temp = temperature_analytics.get_average_temperature(user_input_year)
    max_temp, date_of_max_temp = temperature_analytics.get_max_temperature(user_input_year)
    min_temp, date_of_min_temp = temperature_analytics.get_min_temperature(user_input_year)

    average_temp_formatted = f"{average_temp:.2f}"
    max_temp_formatted = f"{max_temp:.2f}"
    min_temp_formatted = f"{min_temp:.2f}"

    print(f"Průměrná teplota v roce {user_input_year}: {average_temp_formatted}°C")
    print(f"Maximální teplota v roce {user_input_year}: {max_temp_formatted}°C, datum: {date_of_max_temp['den']}.{date_of_max_temp['měsíc']}.{date_of_max_temp['rok']}")
    print(f"Minimální teplota v roce {user_input_year}: {min_temp_formatted}°C, datum: {date_of_min_temp['den']}.{date_of_min_temp['měsíc']}.{date_of_min_temp['rok']}")

elif option == 2:
    user_input_year = temperature_analytics.input_year_value()
    all_monthly_statistics = temperature_analytics.get_all_monthly_statistics(user_input_year)
    
    for month_stat in all_monthly_statistics:
        print(f"\nStatistiky pro {month_names[month_stat['měsíc']]} v roce {user_input_year}:")
        print(f"Průměrná teplota: {month_stat['průměrná teplota']:.2f}°C")
        print(f"Maximální teplota: {month_stat['maximální teplota']:.2f}°C, datum: {month_stat['datum max teploty']}")
        print(f"Minimální teplota: {month_stat['minimální teplota']:.2f}°C, datum: {month_stat['datum min teploty']}")

elif option == 3:
    user_input_year = temperature_analytics.input_year_value()
    user_input_month = temperature_analytics.input_month_value()

    monthly_statistics = temperature_analytics.get_all_monthly_statistics(user_input_year)

    for month_stat in monthly_statistics:
        if month_stat['měsíc'] == user_input_month:
            print(f"\nStatistiky pro {month_names[month_stat['měsíc']]} v roce {user_input_year}:")
            print(f"Průměrná teplota: {month_stat['průměrná teplota']:.2f}°C")
            print(f"Maximální teplota: {month_stat['maximální teplota']:.2f}°C, datum: {month_stat['datum max teploty']}")
            print(f"Minimální teplota: {month_stat['minimální teplota']:.2f}°C, datum: {month_stat['datum min teploty']}")
            break
    else:
        print(f"Pro zadaný měsíc nejsou k dispozici žádné statistiky.")

elif option == 4:
    while True:
        start_year = temperature_analytics.input_year_value()
        end_year = temperature_analytics.input_year_value()
        if start_year < end_year:
            break
    temperature_analytics.plot_annual_temperature_averages(start_year, end_year)

elif option == 5:
    pass
    #tohle už nechávám tobě Víťo

elif option == 6:
    pass
    
elif option == 7:
    temperature_analytics.plot_annual_temperature_averages(1775,2022)
    
elif option == 8:
    user_input_year = temperature_analytics.input_year_value()
    user_input_month = temperature_analytics.input_month_value()
    daily_statistics = temperature_analytics.get_all_daily_statistics(user_input_year,user_input_month)
    temperature_analytics.plot_daily_temperatures(daily_statistics)



elif option == 9:
    user_input_year = temperature_analytics.input_year_value()
    user_input_month = temperature_analytics.input_month_value()
    user_input_day = temperature_analytics.input_day_value()
    day_statistics = temperature_analytics.get_all_daily_statistics(user_input_year,user_input_month)
    temperature_analytics.plot_day_temperatures(day_statistics, user_input_day)
    

else:
    print("Neplatná volba. Ukončuji program.")
