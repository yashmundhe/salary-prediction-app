import streamlit as st
import joblib
import numpy as np

# Load your trained model
model = joblib.load('salary_model.pkl')

st.title('Salary Prediction')
st.write('Predict salary based on years of experience')

years = st.number_input('Years of Experience', min_value=0.0, max_value=50.0, value=5.0, step=0.5)

if st.button('Predict Salary'):
    prediction = model.predict([[years]])[0]
    st.success(f'Predicted Salary: ${prediction:,.2f}')
    
    # Optional: show model info
    st.info(f'Model R² Score: {model.score(X_train, y_train):.3f}')
    