
import streamlit as st
import pandas as pd

# Load dataset
data = pd.read_csv(r"C:\Users\ELCOT\Downloads\clean_data.csv")

st.title("🍴 Simple Restaurant Recommender")

# User input
city = st.selectbox("City", data['city'].unique())
cuisine = st.selectbox("Cuisine", data['cuisine'].unique())

# Filter data
result = data[(data['city'] == city) & (data['cuisine'] == cuisine)]

# Show output
st.write("### Recommended Restaurants")
st.write(result[['name', 'rating', 'cost']].head(5))

