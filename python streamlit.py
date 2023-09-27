import pandas as pd
import streamlit as st
data=pd.DataFrame(
{
    'sr.no':[1,2,3,4,5],
    'gender':['M','F','F','M','M'],
    'WEIGHT':[50,55,60,70,75],
    'HEIGHT':[5.5,5.7,5.8,5.9,5.2]
})

st.table(data)
st.line_chart(data['WEIGHT'])