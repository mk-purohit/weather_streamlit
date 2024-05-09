import requests


def get_data(city, country_code):

    url = f"http://127.0.0.1:8000/forecast/api/?city={city}&country_code={country_code}"
   
    response = requests.get(url)
    data = response.json()
   
    return data

if __name__ == "__main__":
    print(get_data("Kolkata","IN"))
    print(get_data("Dhaka","BD"))
