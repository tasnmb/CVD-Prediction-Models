# Mine, Analyse and Visualise Healthcare Data
This project aims to create an accessable way to find out if a user is at risk of developing CVD or not. This was achieved by data mining a [CVD dataset](https://www.kaggle.com/sulianova/cardiovascular-disease-dataset) and creating a user interface so that the prediction model can be interacted with. 

## Note: 
- All code developed with python version 3.10.11, therefore this version is best to use when running this project

## User Guide:

To use this project:

- Firstly open the command prompt and clone this repo: 
```
git clone https://github.com/tasnmb/CVD-Prediction-Models.git
```
- Install all dependencies used in this project:
```
cd CVD-Prediction-Models
pip install -r requirements.txt
```

## Data Mining:
The data mining process can be found in `/CVD_DataMine/CVD_datamine.ipynb`

This python notebook can be viewed in IDEs such as Visual Studio Code and Jupyter notebook
This part of the project doesn't need to be run (outputs will be the same as outputs that are already visible)

But if one requires the notebook to be run, you could use Jupyter notebook or Visual Studio Code with the Jupyter extension

## User Interface:

To access the UI:

- type `cd CVD_UI` into terminal (make sure your directory is at `CVD-Prediction-Models`, if not `cd CVD-Prediction-Models`)
- then type `python manage.py runserver`
- type `http://localhost:8000/` into your browser and you should be greeted by the home page

To get the recommendations to work, you will need an API key for [NHS API](https://developer.api.nhs.uk/nhs-api) 
Then paste this key into the `get_nhs_recs()` function in `views.py`

Please note that I am working on a more optimised version of this project by utilising feedback given from supervisors. I will include a better way of pasting a users key in (i.e using .env file)


