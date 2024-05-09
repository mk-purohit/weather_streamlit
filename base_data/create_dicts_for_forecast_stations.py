import pandas as pd


 
def create_dictionaries():
    df = pd.read_csv("forecast_stations.csv")
    country_cities = {}
    country_codes = {}

    for index, row in df.iterrows():
        country = row['country']
        city = row['city']
        country_code = row['country_code']

        if country not in country_cities:
            country_cities[country] = [city]
        else:
            country_cities[country].append(city)
        
        if country not in country_codes:
            country_codes[country] = country_code
        # else:
        #     country_codes[country].append(country_code)

    # Write country_cities to file
    with open("country_cities.txt", "w") as f:
        for country, cities in country_cities.items():
            f.write(f"{country}: {', '.join(cities)}\n")
    
    # Write country_codes to file
    with open("country_codes.txt", "w") as f:
        for country, code in country_codes.items():
            f.write(f"{country}: {code}\n")
    
    return country_cities, country_codes


if __name__ == "__main__":
    
    country_cities, country_codes = create_dictionaries()

    print("country_cities:", country_cities)
    print("country_codes:", country_codes)
    





