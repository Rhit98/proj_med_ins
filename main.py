from flask import Flask, jsonify, render_template, request,json
from Project_app.utils import MedicalIns

obj = MedicalIns()
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predictcharges",methods = ["GET"])
def get_insuarance_charges():

    # for raw data(Text)
    # data = json.loads(request.data)

    # for HTML data
    data = request.args.to_dict(flat=True)

    # for form data
    # data = request.form

    print(data)

    return obj.get_predicted_charges(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port="5000",debug=True)