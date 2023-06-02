import pickle
import json
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings("ignore")
import config
import flask



class MedicalIns():
    def __init__(self):
        with open("Project_app/linear_medical.pkl","rb") as f:
            self.model = pickle.load(f)

        with open("Project_app/Json_data.json","r") as f:
            self.json_data = json.load(f)

    def get_predicted_charges(self,data):

        print(data)

        region_index = list(self.json_data['columns']).index("region_" + data["region"])

        test_array = np.zeros(len(self.json_data['columns']))

        test_array[0] = eval(data["age"])
        test_array[1] = self.json_data['sex'][data["sex"]]
        test_array[2] = np.sqrt(eval(data["bmi"]))
        test_array[3] = eval(data["children"])
        test_array[4] = self.json_data['smoker'][data["smoker"]]
        test_array[region_index] = 1

        print("Test Array -->\n", test_array)

        charges = self.model.predict([test_array])[0]

        # for postman
        # charges = str(charges)
        # return f"your charges are {charges}"

        # for HTML
        return flask.render_template("index.html", prediction = charges)