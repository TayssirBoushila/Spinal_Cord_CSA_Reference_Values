import streamlit as st
import pandas as pd

# Load reference values from the Excel file
df_reference = pd.read_excel("merged_reference_values_csa.xlsx")

# Application title
st.title("Normalized CSA Reference Values - Method Comparison")

# Parameter selection
level = st.selectbox("Select Level", df_reference['Level'].unique())
sex = st.selectbox("Select Sex", ["Female", "Male"])
manufacturer = st.selectbox("Select Manufacturer", ["Siemens", "GE", "Philips"])
height_range = st.selectbox("Select Height Range (cm)", df_reference['Height_Range'].unique())

# Filter data based on user selection
filtered_df = df_reference[
    (df_reference['Level'] == level) &
    (df_reference['Sex'] == sex) &
    (df_reference['Manufacturer'] == manufacturer) &
    (df_reference['Height_Range'] == height_range)
]

# Display results for both methods
if not filtered_df.empty:
    st.write(f"**Reference Values for {level}, Sex: {sex}, Manufacturer: {manufacturer}, Height Range: {height_range} cm**")
    
    # Display results for the "nerves" method
    st.subheader("Consecutive Nerve-based Method")
    st.write(f"Mean CSA: {filtered_df['Mean_CSA_nerves'].values[0]:.2f}")
    st.write(f"Confidence Interval: [{filtered_df['CI_Lower_nerves'].values[0]:.2f}, {filtered_df['CI_Upper_nerves'].values[0]:.2f}]")
    
    # Display results for the "vertebral" method
    st.subheader("Vertebral-based Method")
    st.write(f"Mean CSA: {filtered_df['Mean_CSA_vertebral'].values[0]:.2f}")
    st.write(f"Confidence Interval: [{filtered_df['CI_Lower_vertebral'].values[0]:.2f}, {filtered_df['CI_Upper_vertebral'].values[0]:.2f}]")
else:
    st.write("No data available for this selection.")

# To run this application, enter the following command in your terminal:
# streamlit run site.py

