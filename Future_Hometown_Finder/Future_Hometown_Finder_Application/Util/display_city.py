import streamlit as st

from Util.get_img_links import get_img_links

def display_city(row):
    st.header(row.city + ", " + row.state_name)

    img_links = get_img_links(row.city, row.state_name)
    cols=st.columns(2)

    i=0
    for j in range(2):
        for col in cols:
            with col:
                st.image(img_links[i])
            i+=1

    st.write("Population: " + str(row.population))
    st.write("People Per Square Km: " + str(row.density))
    st.write("Estimated Home Price: $" + str(row.estimated_home_price))
    st.write("Average Daytime Temperature: " + str(row.estimated_daytime_temp))
    st.write("Crimes Per Thousand People: " + str(row.crimes_per_thousand_people))
    st.write("Hospital In Town: " + str(row.has_hospital))
    st.text("")
    st.text("")