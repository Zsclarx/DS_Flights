from flask import (Flask,url_for,render_template)
from forms import InputForm
import joblib
import pandas as pd


model = joblib.load(r"flask_proj/model.joblib")

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret_key"

@app.route("/")

@app.route("/home")
def home():
    return render_template("home.html",title = "Home")


@app.route("/predict",methods=["GET","POST"])
def predict():
    form = InputForm()
    if form.validate_on_submit():
        xnew = pd.DataFrame(dict(
            airline  = [form.airline.data],
            date_of_journey  = [form.dateofjoin.data.strftime("%Y-%m-%d")],
            source  = [form.source.data],
            destination  = [form.destination.data],
            dep_time  = [form.dept_time.data.strftime("%H:%M:%S")],
            arrival_time  = [form.arrival_time.data.strftime("%H:%M:%S")],
            duration  = [form.duration.data],
            total_stops  = [form.total_stops.data],
            additional_info  = [form.additional_info.data]
        )
        )
        prediction = model.predict(xnew)[0]
        message = f"The predicted price is INR {prediction} Rs."

    else:
        message = "Please Provide valid input details."
    return render_template("predict.html",title = "Predict",form = form,message = message)



if __name__ == "__main__":
    app.run(debug=True)