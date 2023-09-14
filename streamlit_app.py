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




import snowflake.connector


def load_fruits():
    try:
        # Connect to Snowflake
        conn = snowflake.connector.connect(**snowflake_params)

        # Create a cursor
        cursor = conn.cursor()

        # Execute a SQL query
        cursor.execute("SELECT fruit_name FROM fruits")

        # Fetch the result
        result = cursor.fetchall()

        # Display the result
        result_label.config(text=f"Fruit List: {', '.join([row[0] for row in result])}")

    except snowflake.connector.errors.ProgrammingError as e:
        result_label.config(text=f"Snowflake Error: {e}")
    except Exception as e:
        result_label.config(text=f"An unexpected error occurred: {e}")
    finally:
        # Close the cursor and connection
        cursor.close()
        conn.close()

# Create the main window
root = tk.Tk()
root.title("Snowflake Fruit Query")

# Create a button to load fruits
load_button = tk.Button(root, text="Load Fruits", command=load_fruits)
load_button.pack()

# Create a label to display the result
result_label = tk.Label(root, text="")
result_label.pack()

# Start the GUI main loop
root.mainloop()
