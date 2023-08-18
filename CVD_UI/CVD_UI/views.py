from django.shortcuts import render

import numpy as np
import pandas as pd
import pickle 

import requests, json
from bs4 import BeautifulSoup

# render homepage (which in this case is form for user to fill in)
def home(request):    
    return render(request, 'index.html')


def predict(gender, height, weight, s_blood_pres, d_blood_pres, cholesterol, gluc, smoke, alco, active, age, bmi):
    cvd_model = pickle.load(open('CVD_UI/cvd_model.pkl', 'rb'))
    df_columns = ['gender', 'height', 'weight', 'systolic_blood_pres', 'diastolic_blood_pres', 'cholesterol', 'gluc', 'smoke', 'alco','active', 'age_years', 'BMI']

    # get data in right format for model
    row = np.array([gender, height, weight, s_blood_pres, d_blood_pres, cholesterol, gluc, smoke, alco, active, age, bmi])

    X = pd.DataFrame([row], columns = df_columns)
    prediction = cvd_model.predict(X)

    # instead of just return 1 or 0, unlikely/likely/error are returned (in case of errors)
    if prediction == 0:
        return "unlikely"
    elif prediction == 1:
        return "likely"
    else: 
        return "error"


def calc_bmi(weight, height):
    height = height/100
    return weight/height**2

# returns 'recommmendations' information from the NHS API 
def get_nhs_recs():

    APIKEY = # replace with your actual key

    response = requests.get(
    "https://api.nhs.uk/conditions/cardiovascular-disease/",
    headers={'subscription-key': APIKEY}
    )
    json_object = json.loads(response.text)

    # isolating recommendation data from CVD webpage data in API
    data = json_object['mainEntityOfPage'][3]['mainEntityOfPage'][0]['text']

    # json data stored as HTML so beautiful soup used to store data into easy access array
    soup = BeautifulSoup(data, "html.parser")
    paragraphs = soup.find_all('p')

    # beautifulsoup returns HTML, so conversion to string is needed in order to render 
    recommendations = []

    for i in paragraphs:
        recommendations.append(i.get_text())

    return recommendations


def result(request):
    gender = int(request.GET['gender'])
    height = int(request.GET['height'])
    weight = int(request.GET['weight'])
    systolic_blood_pres = int(request.GET['systolic_blood_pres'])
    diastolic_blood_pres = int(request.GET['diastolic_blood_pres'])
    cholesterol = int(request.GET['cholesterol'])
    gluc = int(request.GET['gluc'])
    smoke = int(request.GET['smoke'])
    alco = int(request.GET['alco'])
    active = int(request.GET['active'])
    age_years = int(request.GET['age_years'])
    bmi = calc_bmi(weight, height)

    result = predict(gender, height, weight, systolic_blood_pres, diastolic_blood_pres, cholesterol, gluc, smoke, alco, active, age_years, bmi)

    if smoke == 1 or active == 0 or alco == 1 or cholesterol > 1 or bmi > 25:
        recommendations = get_nhs_recs()
    else:
        recommendations = None


    return render(request, 'result.html', {'result': result, 'bmi': bmi, 'smoke' : smoke, 'active' : active, 'cholesterol' : cholesterol, 'alco' : alco, 'recommendations' : recommendations})
