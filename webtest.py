import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models
diabetes_model = pickle.load(open('C:/Users/Akash/OneDrive/Desktop/webtest/saved model/diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('C:/Users/Akash/OneDrive/Desktop/webtest/saved model/heart_disease_model.sav','rb'))

# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                          ['Diabetes Prediction',
                           'Heart Disease Prediction',
                           'Causes and Cures'],
                          icons=['activity','heart','info'],
                          default_index=0)
    

# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction using ML')
     
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
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'The person is diabetic'
        else:
          diab_diagnosis = 'The person is not diabetic'
        
    st.success(diab_diagnosis)




# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        sex = st.text_input('Sex')
        
    with col3:
        cp = st.text_input('Chest Pain types')
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
        
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
        
    with col3:
        exang = st.text_input('Exercise Induced Angina')
        
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
        
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
        
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
        
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
        
     
     
    # Initialize heart_prediction
heart_prediction = None

if st.button('Heart Disease Test Result'):
    heart_prediction = heart_disease_model.predict([[int(age), int(sex), int(cp), int(trestbps), int(chol), int(fbs), int(restecg), int(thalach), int(exang), float(oldpeak), int(slope), int(ca), int(thal)]])                          

# Check if heart_prediction is not None before accessing its elements
if heart_prediction is not None and heart_prediction[0] == 1:
    heart_diagnosis = 'The person is having heart disease '
else:
    heart_diagnosis = 'The person does not have any heart disease'

st.success(heart_diagnosis)



# Information Page: Causes and Cures
if selected == 'Causes and Cures':
    st.title('Information on Common Diseases: Causes and Cures')

    # Section on Diabetes
    st.header('Diabetes')
    st.subheader('Causes:')
    st.write("* Genetics: Family history increases the risk.")
    st.write("* Overweight or obesity: Excess weight can impair insulin sensitivity.")
    st.write("* Lack of physical activity: Regular exercise improves insulin use.")
    st.write("* Unhealthy diet: High sugar, unhealthy fats, and processed foods can contribute.")
    st.subheader('Cures:')
    st.write("* While there is no cure, it can be effectively managed through:")
    st.write("    * Healthy lifestyle changes: Balanced diet, regular exercise, weight management.")
    st.write("    * Medication: As prescribed by a doctor, such as insulin or oral medications.")

    # Section on Heart Disease
    st.header('Heart Disease')
    st.subheader('Causes:')
    st.write("* Unhealthy cholesterol levels: High LDL (bad) and low HDL (good) cholesterol.")
    st.write("* High blood pressure: Uncontrolled blood pressure puts strain on the heart.")
    st.write("* Smoking: Damages blood vessels and increases inflammation.")
    st.write("* Diabetes: Contributes to heart disease risk factors like high blood pressure and cholesterol.")
    st.write("* Family history: Genetic predisposition can increase risk.")
    st.write("* Inactivity: Lack of exercise weakens the heart and contributes to other risk factors.")
    st.write("* Unhealthy diet: Obesity, high saturated fat, and low fiber intake increase risk.")
    st.subheader('Cures:')
    st.write("* While there is no definitive cure, it can be prevented and managed through:")
    st.write("    * Healthy lifestyle changes: Balanced diet, regular exercise, smoking cessation.")
    st.write("    * Medication: As prescribed by a doctor, such as cholesterol-lowering medications, blood pressure medications, or blood thinners.")


