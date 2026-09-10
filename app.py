import streamlit as st
import pandas as pd
import joblib


model=joblib.load(
"student_mental_health_model.pkl"
)


st.title(
"AI Student Mental Health Detection System"
)


gender=st.selectbox(
"Gender",
["Male","Female"]
)


age=st.number_input(
"Age",
18,
30
)


course=st.text_input(
"Course"
)


year=st.selectbox(
"Current Year",
[
"Year 1",
"Year 2",
"Year 3",
"Year 4"
]
)


cgpa=st.selectbox(
"CGPA",
[
"0 - 1.99",
"2.00 - 2.49",
"2.50 - 2.99",
"3.00 - 3.49",
"3.50 - 4.00"
]
)


marital=st.selectbox(
"Marital Status",
[
"No",
"Yes"
]
)


anxiety=st.selectbox(
"Anxiety",
[
"Yes",
"No"
]
)


panic=st.selectbox(
"Panic Attack",
[
"Yes",
"No"
]
)



specialist=st.selectbox(
"Visited Specialist",
[
"Yes",
"No"
]
)



if st.button("Predict"):


    input_data=pd.DataFrame({

    'gender':[gender],

    'age':[age],

    'course':[course],

    'year':[year],

    'cgpa':[cgpa],

    'marital_status':[marital],

    'anxiety':[anxiety],

    'panic_attack':[panic],

    'visited_specialist':[specialist]

    })


    prediction=model.predict(input_data)


    if prediction[0]==1:

        st.error(
        "⚠ Student Mental Health Risk Detected"
        )

    else:

        st.success(
        "Student appears to have Low Risk for mental health issue"
        )
