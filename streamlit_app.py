import streamlit as st
import requests

st.title("Fruityvice App")

# Create a dropdown for selecting a fruit
selected_fruit = st.selectbox("Select a fruit:", ["apple", "banana", "cherry"])

# Create a button to fetch fruit information
if st.button("Get Information"):
    if selected_fruit:
        try:
            # Code for fetching fruit information
            response = requests.get(f"https://www.fruityvice.com/api/fruit/{selected_fruit}")
            data = response.json()
            
            # Check if the response contains data
            if 'name' in data:
                fruit_name = data['name']
                st.write(f"The fruit's name is: {fruit_name}")
            else:
                st.error("The 'name' key is not found in the response JSON.")
            
        except requests.exceptions.RequestException as e:
            st.error(f"An error occurred while making the request: {e}")
        except Exception as e:
            st.error(f"An unexpected error occurred: {e}")
    else:
        st.error("Please select a fruit to get information.")





def get_fruityvice_data(fruit_name):
    try:
        # Code for fetching fruit information
        response = requests.get(f"https://www.fruityvice.com/api/fruit/{fruit_name}")
        data = response.json()

        # Check if the response contains data
        if 'name' in data:
            fruit_name = data['name']
            return f"The fruit's name is: {fruit_name}"
        else:
            return "The 'name' key is not found in the response JSON."

    except requests.exceptions.RequestException as e:
        return f"An error occurred while making the request: {e}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"

st.title("Fruityvice App")

# Create a dropdown for selecting a fruit
selected_fruit = st.selectbox("Select a fruit:", ["apple", "banana", "cherry"])

# Create a button to fetch fruit information
if st.button("Get Information"):
    if selected_fruit:
        result = get_fruityvice_data(selected_fruit)
        st.write(result)
    else:
        st.error("Please select a fruit to get information.")
