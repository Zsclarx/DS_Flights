from flask_wtf import FlaskForm
import pandas as pd

from wtforms import (
    SelectField,
    DateField,
    TimeField,
    IntegerField,
    SubmitField,
)

from wtforms.validators import(
    DataRequired,
) 


train = pd.read_csv(r'flask_proj/data/train (1).csv')
val = pd.read_csv(r'flask_proj/data/val.csv')
x_data = pd.concat([train, val],axis=0).drop(columns='price')

class InputForm(FlaskForm):
    airline = SelectField(
        label = 'airline',
        choices= x_data.airline.unique().tolist(),
        validators=[DataRequired()]
    )
    dateofjoin = DateField(
        label = 'date of journey',
        validators=[DataRequired()]
    )
    source = SelectField(
        label = 'Source',
        choices = x_data.source.unique().tolist(),
        validators=[DataRequired()]
    )

    destination = SelectField(
        label = 'Destination',
        choices = x_data.destination.unique().tolist(),
        validators=[DataRequired()]
    )

    dept_time = TimeField(
        label = "Departure Time",
        validators=[DataRequired()]
    )

    arrival_time = TimeField(
        label = "Arrival Time",
        validators=[DataRequired()]
    )

    duration = IntegerField(
        label = "Duration",
        validators=[DataRequired()]
    )

    total_stops = IntegerField(
        label = "Total Stops",
        validators = [DataRequired()]
    )

    additional_info = SelectField(
        label = "Additional Info",
        choices = x_data.additional_info.unique().tolist(),
        validators=[DataRequired()]
    )
    submit = SubmitField(
        label = "Predict"
    )



