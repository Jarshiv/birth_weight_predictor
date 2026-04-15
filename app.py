from flask import Flask,request,jsonify
from flask_cors import CORS
import pandas as pd
import pickle
app=Flask(__name__)
CORS(app)

@app.route("/predict",methods=["post"])
def  get_prediction():
    baby_data=request.get_json()
    baby_df=pd.DataFrame(baby_data)
    with open("model.pkl","rb") as obj:
        model=pickle.load(obj)

    prediction=model.predict(baby_df)
    prediction=round(float(prediction[0]),2)
    response={"prediction":prediction}
    return jsonify(response)

@app.route("/")
def home():
    return "Baby Weight Predictor API - Use POST /predict with baby data"


if __name__ == "__main__":
    app.run(debug=True)