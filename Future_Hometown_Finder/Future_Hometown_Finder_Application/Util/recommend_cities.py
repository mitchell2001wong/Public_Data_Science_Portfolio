import pandas as pd

def recommend_cities(data, state, ideal_pop_size, ideal_pop_density, ideal_home_price, ideal_daytime_temperature, hospital):
    """
    data: The dataset.
    state: The user's preferred state.
    ideal_pop_size: The user's ideal city/town population size.
    ideal_pop_density: Ranges in km**2: Low(0,250), Average(250, 750), High(750, oo), No Preference
    ideal_home_price: The user's ideal home price.
    ideal_daytime_temperature: The user's ideal daytime temperature.
    hospital: Whether or not we care if a hospital is nearby (within the same city/zipcode).
    """
    if (state != "No Preference"):
        data = data[data["state_name"] == state]
        
    if (ideal_pop_density == "Low"):
        data = data[data["density"] <= 250]
    elif (ideal_pop_density == "Average"):
        data = data[250 <= data["density"]]
        data = data[data["density"] <= 750]
    elif (ideal_pop_density == "High"):
        data = data[data["density"] >= 750]

    data["score"] = (abs(data["population"]-ideal_pop_size) / (data["population"]+ideal_pop_size))**2 +\
                    (abs(data["estimated_home_price"]-ideal_home_price) / (data["estimated_home_price"]+ideal_home_price)) +\
                    (abs(data["estimated_daytime_temp"]-ideal_daytime_temperature) / (data["estimated_daytime_temp"]+ideal_daytime_temperature)) +\
                    (data["crimes_per_thousand_people"] / 100)

    # Multiply the current score by 1.5 if there isn't a local hospital
    if(hospital):
        data["score"] = data["score"] + 0.5 * \
            data["score"] * ~data["has_hospital"]

    return data.sort_values("score").reset_index().drop(["index", "score"], axis=1).head(5)