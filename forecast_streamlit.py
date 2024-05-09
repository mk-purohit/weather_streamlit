import streamlit as st
import plotly.express as px
from weather_data.weather_data import get_data



st.title("Weather Forecast for Next 5 Days")

# Hardcoded dictionaries
    
country_cities = {
    'Afghanistan': ['Fayzabad', 'Qala i Naw', 'Pul-e Khumri', 'Mazar-e-Sharif', 'Bamyan', 'Nili', 'Farah', 'Maymana', 'Ghazni', 'Lashkar Gah', 'Herat', 'Sheberghan', 'Kabul', 'Kandahar', 'Khost', 'Asadabad', 'Kunduz', 'Mehtar Lam', 'Pul-i-Alam', 'Jalalabad', 'Zaranj', 'Parun', 'Gardez', 'Bazarak', 'Charikar', 'Sar-e Pol', 'Taloqan', 'Tarinkot', 'Maidan Shar', 'Qalat'], 
    'Bangladesh': ['Dhaka', 'Chittagong', 'Khulna', 'Barisal', 'Sylhet', 'Rajshahi', 'Rangpur', 'Mymensingh', 'Narayanganj', 'Gazipur', 'Narsingdi', 'Tangail', 'Comilla', 'Jessore', 'Kushtia'],
    'Bhutan': ['Jakar', 'Gasa', 'Lhuntse', 'Mongar', 'Paro', 'Pemagatshel', 'Punakha', 'Samdrup Jongkhar', 'Samtse', 'Sarpang', 'Thimphu', 'Trashigang', 'Trashiyangtse', 'Trongsa', 'Damphu', 'Wangdue Phodrang', 'Zhemgang', 'Phuentsholing', 'Bajo', 'Gyelposhing'],
    'India': ['Amaravati', 'Itanagar', 'Dispur', 'Patna', 'Raipur', 'Panaji', 'Gandhinagar', 'Chandigarh', 'Shimla', 'Ranchi', 'Bengaluru', 'Thiruvananthapuram', 'Bhopal', 'Mumbai', 'Imphal', 'Shillong', 'Aizawl', 'Kohima', 'Bhubaneswar', 'Chandigarh', 'Jaipur', 'Gangtok', 'Chennai', 'Hyderabad', 'Agartala', 'Lucknow', 'Dehradun', 'Kolkata', 'Port Blair', 'Chandigarh', 'Daman', 'Kavaratti', 'New Delhi', 'Puducherry', 'Leh', 'Kavaratti', 'Srinagar', 'Pune', 'Ahmedabad', 'Surat', 'Kanpur', 'Nagpur', 'Indore', 'Thane', 'Bhopal', 'Visakhapatnam', 'Vadodara', 'Ghaziabad', 'Ludhiana', 'Agra', 'Nashik', 'Faridabad', 'Meerut', 'Rajkot', 'Varanasi', 'Aurangabad', 'Dhanbad', 'Jammu'],
    'Maldives': ['Male', 'Hithadhoo', 'Mahibadhoo', 'Eydhafushi', 'Naifaru', 'Muli', 'Kudahuvadhoo', 'Thinadhoo', 'Dhidhdhoo', 'Kulhudhuffushi', 'Vilufushi'],
    'Myanmar': ['Hakha', 'Myitkyina', 'Loikaw', 'Hpa-An', 'Mawlamyine', 'Sittwe', 'Taunggyi', 'Pathein', 'Bago', 'Magway', 'Mandalay', 'Sagaing', 'Dawei', 'Yangon', 'Naypyidaw', 'Pyin Oo Lwin'],
    'Nepal': ['Biratnagar', 'Janakpur', 'Hetauda', 'Pokhara', 'Butwal', 'Birendranagar', 'Dipayal Silgadhi', 'Kathmandu', 'Dharan', 'Bharatpur', 'Birgunj', 'Dhangadhi', 'Nepalgunj'],
    'Pakistan': ['Lahore', 'Karachi', 'Peshawar', 'Quetta', 'Islamabad', 'Faisalabad', 'Rawalpindi', 'Multan', 'Hyderabad', 'Sialkot', 'Gujranwala', 'Larkana', 'Bahawalpur', 'Sargodha', 'Mirpur Khas', 'Gujrat', 'Mardan', 'Kohat', 'Sheikhupura', 'Jhang'],
    'Sri Lanka': ['Kandy', 'Trincomalee', 'Anuradhapura', 'Jaffna', 'Kurunegala', 'Ratnapura', 'Galle', 'Badulla', 'Colombo', 'Gampaha', 'Matara', 'Batticaloa', 'Kalmunai', 'Kegalle', 'Sri Jayawardenepura Kotte'],
}

country_codes = {
    'Afghanistan': 'AF',
    'Bangladesh': 'BD',
    'Bhutan': 'BT',
    'India': 'IN',
    'Maldives': 'MV',
    'Myanmar': 'MM',
    'Nepal': 'NP',
    'Pakistan': 'PK',
    'Sri Lanka': 'LK',
}


# Create two columns for layout
col1, col2 = st.columns(2)

# Select box for country
selected_country = col1.selectbox("Select a country", list(country_cities.keys()))

# Select box for city
if selected_country:
    selected_city = col2.selectbox("Select a city", country_cities[selected_country])
    
    if selected_city:
        st.write("Country Code:", country_codes[selected_country])
        st.write("City:", selected_city)

place = selected_city
code = country_codes[selected_country]

st.subheader(f"3 Hourly Temperature (C) Forecast for {place}, {selected_country}")


try:
    data = get_data(place, code)

    dates = data["local_dates_text"]
    temperatures = data['temperature']
    
    figure = px.line(x=dates, y=temperatures, labels={'x':'Dates', 'y':'Temperature (C)'})
    st.plotly_chart(figure)

except KeyError:
    st.write("That place does not exist")