import streamlit as st
import flask
import os

app = flask.Flask(__name__)
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))

    if port == 5000:
        app.debug = True
    app.run(host='0.0.0.0', port=port)

#streamlit run "C:\Users\lyh39\Desktop\enroll tool\admit_enroll.py"

Gender=st.sidebar.selectbox('Select Gender', ['Female', 'Male'])
Age=st.sidebar.selectbox('Select Age', ['<17', '18', '19', '>19'])
Race=st.sidebar.selectbox('Select Race', ['Asian', 'Not Specified', 'URM', 'White'])
Citizenship=st.sidebar.selectbox('Select Citizenship', ['Permanent Resident', 'Alien Temporary', 'Not Indicated', 'Native'])
Residency=st.sidebar.selectbox('Select Residency', ['Out of State', 'In State'])
ACT_Score=st.sidebar.selectbox('Select ACT Score', ['<=21', '22-24', '25-28', '>=29', 'Not Provided'])
High_School_GPA=st.sidebar.selectbox('Select High School GPA', ['<=3.2', '3.2-3.6', '3.6-3.9', '>3.9', 'Not Provided'])
Number_of_Days=st.sidebar.selectbox('Select Days between Application and Admission Date', ['<=3 days', '>3 days'])
Priority_Date=st.sidebar.selectbox('Select Apply before Priority Date', ['Yes', 'No'])
Application_Fee_Status=st.sidebar.selectbox('Select Application Fee Status', ['Pending', 'Waived', 'Received'])

if Gender in ['Female', 'Male']:
    A=0

if Age in ['<17', '18', '19']:
    B=0
if Age=='>19':
    B=0.5569

if Race=='Asian':
    C=-0.8333
if Race=='URM':
    C=-0.4295
if Race=='Not Specified':
    C=-0.5802
if Race=='White':
    C=0

if Citizenship=='Permanent Resident':
    D=-0.491
if Citizenship=='Alien Temporary':
    D=0.3856
if Citizenship in ['Not Indicated', 'Native']:
    D=0

if Residency=='In State':
    E=0
if Residency=='Out of State':
    E=-1.087

if ACT_Score=='>=29':
    F=-0.2303
if ACT_Score=='Not Provided':
    F=-1.4634
if ACT_Score in ['22-24', '25-28', '<=21']:
    F=0

if High_School_GPA=='>3.9':
    G=0.1335
if High_School_GPA=='Not Provided':
    G=-2.5495
if High_School_GPA in ['<=3.2', '3.2-3.6', '3.6-3.9']:
    G=0

if Number_of_Days=='<=3 days':
    H=0
if Number_of_Days=='>3 days':
    H=-0.4312

if Priority_Date=='Yes':
    I=0
if Priority_Date=='No':
    I=0.4192

if Application_Fee_Status=='Waived':
    J=-1.2021
if Application_Fee_Status in ['Pending', 'Received']:
    J=0


log_odds=1.3568+A+B+C+D+E+F+G+H+I+J
odds=2.71828**log_odds
probability=odds/(odds+1)


st.write("Log Odds of Enrollment:", '{0:.4f}'.format(log_odds))
st.write("Odds of Enrollment:", '{0:.4f}'.format(odds))
st.write("Probability of Enrollment:", '{:.2%}'.format(probability))
st.text("*If Probability of Enrollment>50%, usually expect the applicant to enroll")
