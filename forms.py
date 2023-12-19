from flask_wtf import FlaskForm
from wtforms import SelectField, IntegerField, FloatField, SubmitField
from wtforms.validators import DataRequired

class InputForm(FlaskForm):
    gender = SelectField('Gender', choices=[('', 'Please select'), ('Male', 'Male'), ('Female', 'Female'), ('other', 'Other')], validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired()])
    hypertension = SelectField('Does the patient have hypertension?', choices=[('', 'Please select'), ('1', 'Yes'), ('0', 'No')], validators=[DataRequired()])
    heart_disease = SelectField('Does the patient have heart diseases?', choices=[('', 'Please select'), ('1', 'Yes'), ('0', 'No')], validators=[DataRequired()])
    ever_married = SelectField('Has the patient ever married?', choices=[('', 'Please select'), ('Yes', 'Yes'), ('No', 'No')], validators=[DataRequired()])
    work_type = SelectField('What is type of work does the patient?', choices=[('', 'Please select'), ('Private', 'Private'), ('Self-employed', 'Self Employed'), ('children', 'Taking care of Children'), ('Govt_job', 'Government Job'), ('Never_worked', 'Never Worked')], validators=[DataRequired()])
    residence = SelectField('What kind of residence area does the patient have?', choices=[('', 'Please select'), ('Urban', 'Urban'), ('Rural', 'Rural')], validators=[DataRequired()])
    glucose_level = FloatField("Patient's average blood glucose level", validators=[DataRequired()])
    bmi = FloatField("Patient's Body Mass Index (BMI)", validators=[DataRequired()])
    smoke_status = SelectField("Patient's smoking status", choices=[('', 'Please select'), ('smokes', 'Currently smokes'), ('never smoked', 'Never Smoked'), ('Unknown', 'Not Known'), ('formerly smoked', 'Smoked in the past')], validators=[DataRequired()])
    submit = SubmitField("Submit")
