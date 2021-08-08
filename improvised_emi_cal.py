import streamlit as st

@st.cache()
def calculate_emi(p, n, r):
  return round(p*(r/100)*((1+(r/100))**n/((1+(r/100))**n - 1)),2)

@st.cache()
def calculate_outstanding_balance(p, n, r, m):
  return round((p*((r/100)**n) - ((1+(r/100))**m))/((1+(r/100))**n - 1),2)

st.title('EMI Calaculator')
principal = st.sidebar.slider('Principal Loan Amount',1000,100000)
tenure = st.sidebar.slider('Loan Period(in years)',1,30)
n = tenure*12
roi = st.sidebar.slider('Rate of Interest(in % per annum)',1,15)
r = roi/12
m = st.sidebar.slider('Period after which the Outstanding Loan Balance is calculated (in months)',1,n,(0.25,0.5,0.75))
if st.sidebar.button('Calculate EMI'):
  'Your EMI is : ',calculate_emi(principal, n, r)
if st.sidebar.button('Calculate Outstaning Loan Balance'):
  'Your Outstanding Loan Balance is : ',calculate_outstanding_balance(principal, n, r, m)