import streamlit as st
import pandas as pd
import numpy as np

def main():
    st.sidebar.title("Navigation")
    user_choice = st.sidebar.radio('Go to', ('Home', 'Heart Disease Prediction'))

    if user_choice == 'Home':
        st.title('Welcome to the Heart Disease Prediction System')
        st.write('This System uses machine learning to predict heart disease.')

    elif user_choice == 'Heart Disease Prediction':
        st.title('Heart Disease Prediction')

        # Here you can add your input fields and prediction logic

if __name__ == "__main__":
    main()
