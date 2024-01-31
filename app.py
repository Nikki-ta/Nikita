from flask import Flask, jsonify, render_template, request
import joblib
import os
import numpy as np

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("home.html")

@app.route('/predict',methods=['POST','GET'])
def result():

    evaporation_from_vegetation_transpiration_sum= float(request.form['evaporation_from_vegetation_transpiration_sum'])
    soil_temperature_level_1=float(request.form['soil_temperature_level_1'])
    surface_net_solar_radiation_sum=float(request.form['surface_net_solar_radiation_sum'])
    temperature_2m= float(request.form['temperature_2m'])
    total_precipitation_sum=float(request.form['total_precipitation_sum'])


    X= np.array([[evaporation_from_vegetation_transpiration_sum,soil_temperature_level_1, surface_net_solar_radiation_sum,
                 temperature_2m, total_precipitation_sum]])

    # scaler_path='sc.sav'

    # sc=joblib.load(scaler_path)

    # X_std= sc.transform(X)

    model_path='mlr.sav'

    model= joblib.load(model_path)

    Y_pred=model.predict(X)

    area = 206066.10

    crop_yield = output(area,Y_pred)
    crop_yield = round(crop_yield, 3)
    # return jsonify({'PREDICTED YIELD IN KG-HECTARES': float(crop_yield)})
    return render_template('predict.html', predicted_output=crop_yield)

def output(area,Y_pred):
        m = 5
        c = 5.0

        yield_pred = m * Y_pred + c
        # yield_act = m * test_y + c

        # calculate total predicted crop yield in tonnes
        crop_yield = np.sum(yield_pred) * area

        # calculate total actual crop yield in tonnes
        # crop_yield_act = np.sum(yield_act) * area_hectares

        # predicted average yearly crop yield in million tonnes
        crop_yield = (crop_yield)/1000000

        return crop_yield

        # # Actual average yearly crop yield in million tonnes
        # crop_yield_act = (crop_yield_act/8)/1000000


if __name__ == "__main__":
    app.run(debug=True, port=9457)