import numpy as np
import pickle
import pandas as pd
import streamlit as st

pickle_in = open("rf.pk1", "rb")
rf = pickle.load(pickle_in)

def predict_fuel_efficiency(Eng_Displ, Cyl, Gears, Max_Ethanol, Intake_Valves_Per_Cyl, Exhaust_Valves_Per_Cyl, Trans_Creeper_Gear, Trans_Desc, Carline_Class_Desc, Label_Recalc, Stop_Start):
    prediction = rf.predict([[Eng_Displ, Cyl, Gears, Max_Ethanol, Intake_Valves_Per_Cyl, Exhaust_Valves_Per_Cyl, Trans_Creeper_Gear, Trans_Desc, Carline_Class_Desc, Label_Recalc, Stop_Start]])
    return prediction
def main():
    st.title("Fuel efficiency prediction")
    Eng_Displ = st.text_input("Eng_Displ", "Type here")
    Cyl = st.text_input("Cyl", "Type here")
    Gears = st.text_input("Gears", "Type here")
    Max_Ethanol = st.text_input("Max_Ethanol", "Type here")
    Intake_Valves_Per_Cyl = st.text_input("Intake_Valves_Per_Cyl", "Type here")
    Exhaust_Valves_Per_Cyl = st.text_input("Exhaust_Valves_Per_Cyl", "Type here")
    Trans_Creeper_Gear = st.text_input("Trans_Creeper_Gear", "Type here")
    Trans_Desc = st.text_input("Trans_Desc", "Type here")
    Carline_Class_Desc = st.text_input("Carline_Class_Desc", "Type here")
    Label_Recalc = st.text_input("Label_Recalc", "Type here")
    Stop_Start = st.text_input("Stop_Start", "Type here")
    result = ""
    if st.button("Predict"):
        result= predict_fuel_efficiency(Eng_Displ, Cyl, Gears, Max_Ethanol, Intake_Valves_Per_Cyl, Exhaust_Valves_Per_Cyl, Trans_Creeper_Gear, Trans_Desc, Carline_Class_Desc, Label_Recalc, Stop_Start)
    st.success('The output is {}'.format(result))
if __name__ == '__main__':
    main()
