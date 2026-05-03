import streamlit as st
import pandas as pd
import numpy as np


st.title("Hello This is a basic of streamlit by Monojit Nandy")

#st.subheader("Brewed with steamlit")
st.text("Welcome to your fist interative app")
st.write("Choose your fav. Variety of language:")

programming=st.selectbox("Your Fav pogramming language: ",["JAVA","C/C++","JAVASCRIPT","HTML","CSS","NODE.JS","NEXT.JS","EXPRESS.JS","NPM","PANDAS","MATPLOT","NUMPY","SEABORN"])
st.write(f"You fav programming language is {programming}. Excellent choice")
st.success("Your programming language has been choose")

#csv file input
st.title("Chai sales Dashboard")
file = st.file_uploader("Upload you csv file", type=["csv"])

if file:
    df = pd.read_csv(file)
    st.subheader("Data previewer")
    st.dataframe(df)
if file:
    st.subheader("Summary Stats")
    st.write(df.describe())

    #pandas part
if file:
    cities = df["city"].unique()
    selected_city = st.selectbox("Filter by cities", cities)
    filteed_data = df[df["city"] == selected_city]
    st.dataframe(filteed_data)



st.sidebar.header("Patient Information")

hba1c_start = st.sidebar.slider(
    "Starting HbA1c",
    4.0, 15.0, 7.0
)

auralin_used = st.sidebar.selectbox(
    "Auralin",
    [0, 1]
)

novodra_used = st.sidebar.selectbox(
    "Novodra",
    [0, 1]
)

auralin_effect = hba1c_start * auralin_used
novodra_effect = hba1c_start * novodra_used

if auralin_used == 1 and novodra_used == 0:
    treatment_type = 1
elif auralin_used == 0 and novodra_used == 1:
    treatment_type = 2
elif auralin_used == 1 and novodra_used == 1:
    treatment_type = 3
else:
    treatment_type = 0

hba1c_start_sq = hba1c_start ** 2

features = np.array([[
    hba1c_start,
    hba1c_start_sq,
    auralin_used,
    novodra_used,
    auralin_effect,
    novodra_effect,
    treatment_type
]])
col1, col2, col3 = st.columns(3)

col1.metric("Starting HbA1c", round(hba1c_start, 2))
col2.metric("Auralin", auralin_used)
col3.metric("Novodra", novodra_used)

st.write("")

st.set_page_config(page_title="BMI Calculator")

st.title("Patient BMI Calculator")

height = st.slider(
    "Height (cm)",
    120,
    220,
    170
)

weight = st.slider(
    "Weight (kg)",
    30,
    200,
    70
)

# BMI formula
bmi = weight / ((height/100) ** 2)

st.metric("BMI", round(bmi, 2))

# category
if bmi < 18.5:
    st.warning("Underweight")
elif bmi < 25:
    st.success("Normal")
elif bmi < 30:
    st.warning("Overweight")
else:
    st.error("Obese")


    st.set_page_config(page_title="Patient Dashboard", layout="wide")

st.title("Patient Dashboard")

df = pd.read_csv("patients.csv")

patient_id = st.text_input("Enter Patient ID")

if patient_id:
    patient = df[df["patient_id"].astype(str) == patient_id]

    if not patient.empty:
        row = patient.iloc[0]

        st.success("Patient Found")

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Basic Info")
            st.write("**Name:**", row["given_name"], row["surname"])
            st.write("**Sex:**", row["assigned_sex"])
            st.write("**DOB:**", row["birthdate"])
          

        with col2:
            st.subheader("Health Info")
            st.write("**Height:**", row["height"])
            st.write("**Weight:**", row["weight"])
            st.write("**BMI:**", row["bmi"])

        st.subheader("Address")
        st.write(row["address"])
        st.write(row["city"], ",", row["state"], ",", row["country"])

        st.subheader("Contact")
        st.write(row["contact"])

    else:
        st.error("Patient ID not found")


