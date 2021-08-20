import pandas as pd
import streamlit as st

from Util.recommend_cities import recommend_cities
from Util.display_city import display_city

data = pd.read_csv("Future_Home_Location_Data.zip")


st.title("Future Hometown Finder")

st.write("""
## Complete the fields below to find your future hometown!
### Note that if we cannot find a city/town which exactly fits your criteria, we will return results which best match your preferences.
""")

state = st.selectbox(
    "Choose a Preferred State (Optional):",
    ("No Preference", "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware",
     "District of Columbia", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas",
     "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota",
     "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York",
     "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania",
     "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia",
     "Washington", "West Virginia", "Wisconsin", "Wyoming")
)

ideal_pop_size = st.number_input(
    "What is your ideal city/town population size?")

ideal_pop_density = st.selectbox(
    "What is your ideal population density?", ("No Preference", "Low", "Average", "High"))

ideal_home_price = st.number_input("What is your ideal home price?")

ideal_daytime_temperature = st.number_input(
    "What is your ideal daytime temperature in degrees fahrenheit?")

hospital = st.selectbox(
    "Do you care if there is a hospital in town?", ("Yes", "No"))


# On submit, display best cities
if(st.button("Submit")):
    recommended_cities = recommend_cities(data, state, ideal_pop_size, ideal_pop_density,
                                          ideal_home_price, ideal_daytime_temperature, hospital)

    recommended_cities.apply(display_city, axis=1)
