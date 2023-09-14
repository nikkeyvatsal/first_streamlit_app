
import streamlit
import pandas
import requests
import snowflake.connector
import urllib.request



streamlit.title('My new code page')

streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')


#import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')





#import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response);






# write your own comment -data is normalized
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - normalizied as fruit vice
streamlit.dataframe(fruityvice_normalized)



fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

streamlit.stop()
#import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
my_data_row = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_row)


my_cur.execute("insert into fruit_load_list values ('From streamlit')")





import requests
streamlit.header('Fruityvice Fruit Advice!')
try:
    # Code that might raise an exception
    fruit_choice = streamlit.text_input("what fruit would you like information about?")
    
    if not fruit_choice:
        fruit_choice = response.json()
        
        # Check if the 'name' key exists in the JSON response
        if 'name' in data:
            fruit_name = data['name']
            print(f"The fruit's name is: {fruit_name}")
        else:
          fruitvice_response= request.get("https://fruityvice.com/api/fruit/" +fruit_choice)
          fruityvice_normalized = pandas.json_normalize(fruitvice_response.json())
          streamlit.dataframe(fruityvice_normalized)
          
  
        
except requests.exceptions.RequestException as e:
    print(f"An error occurred while making the request: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")





