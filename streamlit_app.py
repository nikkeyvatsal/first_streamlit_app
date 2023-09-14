import streamlit as st
import requests


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


def load_fruit_list():
    try:
        # Connect to Snowflake
        conn = snowflake.connector.connect(**snowflake_params)

        # Create a cursor
        cursor = conn.cursor()

        # Execute a SQL query to fetch the fruit list
        cursor.execute("SELECT fruit_name FROM fruits")

        # Fetch the result
        fruit_list = cursor.fetchall()

        # Display the result
        st.write("Fruit List:")
        for row in fruit_list:
            st.write(row[0])

    except snowflake.connector.errors.ProgrammingError as e:
        st.error(f"Snowflake Error: {e}")
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")
    finally:
        # Close the cursor and connection
        cursor.close()
        conn.close()

# Create a Streamlit app
st.title("Snowflake Fruit List")
st.sidebar.button("Load Fruit List", on_click=load_fruit_list)

result_text.pack()

# Start the GUI main loop
root.mainloop()


