# -*- coding: utf-8 -*-
"""
Created on Wed Apr  2 01:48:34 2025

@author: Dell
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu



# loading the saved models

diabetes_model_one = pickle.load(open('trained_model.sav', 'rb'))

diabetes_model_two = pickle.load(open('trained_model (3).sav', 'rb'))





# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Diabetes Prediction System',
                           
                           ['Prediction for Old Generation',
                            'Prediction for Pregnant Ladies'
                               ],
                           icons=['activity','heart','person'],
                           default_index=0)
    
    
# diabetes Prediction Page
if(selected == 'Prediction for Old Generation'):
    # page title
    st.title('Diabetes Prediction for Dataset - 1')
        
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
        
    with col1:
        gender = st.text_input('Gender of the Person')
            
    with col2:
        age = st.text_input('Age of the Person')
            
    with col3:
        hypertension = st.text_input('Hypertension') 
            
    with col1:
        heart_disease = st.text_input('Heart Disease')    
            
    with col2:
        smoking_history = st.text_input('Smoking History')    
            
    with col3:
        bmi = st.text_input('BMI value')    
            
    with col1:
        HbA1c_level = st.text_input('HbA1c level of the Person')    
            
    with col2:
        blood_glucose_level = st.text_input('Glucose level of the Person')    
            
  
        
  
            
    # code for Prediction
    diab_diagnosis = ''
        
    # creating a button for Prediction
        
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model_one.predict([gender, age, hypertension, heart_disease, smoking_history, bmi, HbA1c_level, blood_glucose_level])
        
        if(diab_prediction[0] == 1):
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'
                
    st.success(diab_diagnosis)
        
    
    
    
    
    # diabetes prediction for pregnant ladies
    if(selected == 'Prediction for Pregnant ladies'):
        # page title
        st.title('Diabetes Prediction for Dataset - 2')
            
        # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    
    with col2:
        Insulin = st.text_input('Insulin Level')
    
    with col3:
        BMI = st.text_input('BMI value')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
    with col2:
        Age = st.text_input('Age of the Person')
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model_two.predict([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'The person is diabetic'
        else:
          diab_diagnosis = 'The person is not diabetic'
        
    st.success(diab_diagnosis)

            
        
        
 
       
        

            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        