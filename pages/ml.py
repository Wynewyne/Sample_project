import streamlit as st
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
rfmodel= st.sidebar.checkbox('Decision Trees')
data = pd.read_csv('buycomputer.csv')

if rfmodel:
    
    with st.form("my_form1"):
        
        st.title('Classify the new circustances')
        
        st.subheader("Please Choose Customer Circustances")
        agegp = st.selectbox("What's customer Age:", ['youth', 'middle_aged', 'senior'])

        student = st.radio("Is customer Student:", ['yes', 'no'])
    
        income = st.selectbox("What's customer income:", data['income'].unique())
        credit_rating = st.radio("customer credit rating:", ['excellent', 'fair'])
        st.write("You selected:", "Age:" + agegp + "Student:" + student)
    
    
        
        submitted = st.form_submit_button("Submit")
        if submitted:
            #st.write("slider", slider_val, "checkbox", checkbox_val)
            inputdata = {'age': agegp,
                        'studen': student, 
                        'income': income,
                        'credit rating': credit_rating}
            features = pd.DataFrame(inputdata, index=[0])
            features_dummy = pd.get_dummies(features)
            #st.write(features)
            #################################################
            
            X = data[['age', 'income', 'studen', 'credit rating']]
            y = data[['class']]
            X_dummies = pd.get_dummies(X)
            X_train, X_test, y_train, y_test = train_test_split(X_dummies,y,test_size=0.25, random_state=25)
            ##################################################
            # load model
            filename = 'test1'
            loaded_model = pickle.load(open(filename, "rb"))
            testsdata1=pd.get_dummies(features_dummy)
            testsdata2 =  testsdata1.reindex(columns =  X_train.columns, fill_value=0)
            clfres = loaded_model.predict(testsdata2)
            if clfres == 'yes':
                st.write('The customer will buy the computer')
            else:
                st.write('The customer will not buy the computer')
            
           
            
           
            


   
