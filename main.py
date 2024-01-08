import streamlit as st
import pandas as pd
import numpy as np
import joblib


def main():
    st.sidebar.title("Navigation")
    user_choice = st.sidebar.radio('Go to', ('Home', 'Heart Disease Prediction'))

    if user_choice == 'Home':
        st.title('Welcome to the Heart Disease Prediction System')
        st.write('This System uses machine learning to predict heart disease.')
        st.image('CVD.PNG', use_column_width=True)

        st.header('About Cardiovascular Disease (CVD)')
        st.write('''
        Cardiovascular Disease (CVD) encompasses a range of conditions affecting the heart and blood vessels. It is one of the leading causes of death globally. Common types of CVD include coronary artery disease, stroke, heart failure, arrhythmias, and heart valve problems.

        **Key Causes:**
        - High blood pressure
        - Smoking
        - High cholesterol
        - Diabetes
        - Sedentary lifestyle
        - Poor diet
        - Obesity
        - Family history of heart disease

        **Symptoms to Watch For:**
        - Chest pain or discomfort (angina)
        - Shortness of breath
        - Nausea, indigestion, or heartburn
        - Pain or discomfort in the arms, neck, jaw, back, or upper stomach
        - Lightheadedness, dizziness, or fainting
        - Rapid or irregular heartbeats

        Early detection and management of these risk factors are crucial for the prevention and treatment of CVD. Our prediction system aims to identify potential risks of heart disease based on various health parameters, enabling timely intervention and care.
        ''')


    elif user_choice == 'Heart Disease Prediction':
        st.title('Heart Disease Prediction')
        st.image('CVD2.PNG', use_column_width=True)

        # Input fields for user data
        age = st.text_input('Age', '')
        weight = st.text_input('Weight (kg)', '')
        bmi = st.text_input('BMI', '')
        sex = st.selectbox('Sex', options=['Male', 'Female'])
        diabetes = st.selectbox('Diabetes', options=['Yes', 'No'])
        exercise = st.selectbox('Exercise', options=['Yes', 'No'])

        # Convert inputs to appropriate data types and handle categorical data
        try:
            age = int(age)
            weight = float(weight)
            bmi = float(bmi)
            sex = 1 if sex == 'Male' else 0
            diabetes = 1 if diabetes == 'Yes' else 0
            exercise = 1 if exercise == 'Yes' else 0

            if st.button('Predict'):
                # Load your pre-trained model
                model = joblib.load('ensemble_model.pkl')

                # Make prediction
                features = np.array([exercise, bmi, diabetes, sex, age, weight])
                prediction = model.predict([features])

                # Display prediction
                st.write('Prediction: ',
                         'Positive for Heart Disease' if prediction[0] == 1 else 'Negative for Heart Disease')

        except ValueError:
            st.write("Please enter valid values")


if __name__ == "__main__":
    main()
