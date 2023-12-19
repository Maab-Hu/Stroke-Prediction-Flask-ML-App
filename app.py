from flask import Flask, render_template,request, redirect, url_for
import pickle
from flask_wtf import FlaskForm
from wtforms import SelectField
from forms import InputForm
from utils import get_prediction


class GenderForm(FlaskForm):
    gender = SelectField('Gender', choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')])

app = Flask(__name__)

transformer = pickle.load(open("models/transformer.pkl","rb"))
pipes = pickle.load(open("models/pipes.pkl","rb"))

app.config['SECRET_KEY'] = 'Eight-Handled Sword Divergent Sila Divine General Mahoraga'

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        model = request.form['button_type']

        if model == 'Logistic Regression':
            return redirect(url_for('logistic_regression_route'))
        elif model == 'Decision Tree':
            return redirect(url_for('decision_tree_route'))
        elif model == 'Support Vector Machine':
            return redirect(url_for('svm_route'))
        else:
            return redirect(url_for('home'))
    else:
        return redirect(url_for('home'))

@app.route('/logistic_regression', methods=['GET', 'POST'])
def logistic_regression_route():

    form = InputForm()
    prediction = None
        
    if form.validate_on_submit():
            
            gender = form.gender.data
            age = form.age.data
            hypertension = form.hypertension.data
            heart_disease = form.heart_disease.data
            ever_married = form.ever_married.data
            work_type = form.work_type.data
            residence = form.residence.data
            glucose_level = form.glucose_level.data
            bmi = form.bmi.data
            smoke_status = form.smoke_status.data

            user_data = [gender, age, hypertension, heart_disease, ever_married, work_type, residence, glucose_level, bmi, smoke_status]

            prediction = get_prediction(model='Logistic Regression',input=user_data)

    return render_template("predict.html",form=form, prediction=prediction)

@app.route('/decision_tree', methods=['GET', 'POST'])
def decision_tree_route():
    form = InputForm()
    prediction = None

    if form.validate_on_submit():
            
            gender = form.gender.data
            age = form.age.data
            hypertension = form.hypertension.data
            heart_disease = form.heart_disease.data
            ever_married = form.ever_married.data
            work_type = form.work_type.data
            residence = form.residence.data
            glucose_level = form.glucose_level.data
            bmi = form.bmi.data
            smoke_status = form.smoke_status.data

            user_data = [gender, age, hypertension, heart_disease, ever_married, work_type, residence, glucose_level, bmi, smoke_status]

            prediction = get_prediction(model='Decision Tree',input=user_data)

    return render_template("predict.html",form=form, prediction=prediction) 

@app.route('/svm', methods=['GET', 'POST'])
def svm_route():
    form = InputForm()
    prediction = None
        
    if form.validate_on_submit():
            
            gender = form.gender.data
            age = int(form.age.data)
            hypertension = int(form.hypertension.data)
            heart_disease = int(form.heart_disease.data)
            ever_married = form.ever_married.data
            work_type = form.work_type.data
            residence = form.residence.data
            glucose_level = float(form.glucose_level.data)
            bmi = float(form.bmi.data)
            smoke_status = form.smoke_status.data

            user_data = [gender, age, hypertension, heart_disease, ever_married, work_type, residence, glucose_level, bmi, smoke_status]

            print(user_data)

            prediction = get_prediction(model='Support Vector Machine',input=user_data)

            print(prediction)

    return render_template("predict.html",form=form, prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)



