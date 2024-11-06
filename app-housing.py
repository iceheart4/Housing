import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt



st.title('California Housing Data(1990)')
df = pd.read_csv('housing.csv')

# note that you have to use 0.0 and 40.0 given that the data type of population is float
price_filter = st.slider('Minimal Median house price:', 0.0, 500001.0, 200000.0)  # min, max, default




# create a multi select
ocean_proximity = st.sidebar.multiselect(
     'Choose the location type',
     df.ocean_proximity.unique(),  # options
     df.ocean_proximity.unique())  # defaults

# Radio button for income level
income_level = st.sidebar.radio(
    "Choose income level",
    ('Low (≤2.5)', 'Medium (> 2.5 & < 4.5)', 'High (> 4.5)')
)

# filter by price
df = df[df.median_house_value >= price_filter]

# Filter by income level
if income_level == 'Low (≤2.5)':
    df = df[df.median_income <= 2.5]
elif income_level == 'Medium (> 2.5 & < 4.5)':
    df = df[(df.median_income > 2.5) & (df.median_income < 4.5)]
else:
    df = df[df.median_income > 4.5]

# show on map
st.map(df)

# Plot histogram
# Filter the dataframe based on the slider value
filtered_df = df[df['median_house_value'] >= price_filter]

st.subheader('Histogram of Median House Value')
plt.hist(filtered_df['median_house_value'], bins=30)
st.pyplot(plt)
