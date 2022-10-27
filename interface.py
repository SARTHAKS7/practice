from flask import Flask,jsonify,request,render_template,redirect, url_for
from project_app.utils import MedicalInsurance
print("newjewdhba")

print("i m here")

import config

app = Flask(__name__)
#############################################################################################
################################ Home API ###################################################
#############################################################################################

@app.route("/")   # Home API
def hello_flask():
    print("Welcome to flask")
    #return "Hello Python"
    return render_template("login.html")


@app.route('/result')
def result():
    return "Successful"    



@app.route("/login",methods =["POST",'GET'] )
def login():
    if request.method == 'POST':
        data = request.form 
        name = data["name"]
        print("Name ::",name)
        return redirect(url_for('result',name= name))


    if request.method == 'GET':
        data = request.args.get("name") 
        name = data["name"]
        print("Name ::",name)
        return redirect(url_for('result',name= name))








@app.route('/marks/<float:score>')
def mark(score):
    return f"Hello {score}"  

#############################################################################################
################################ Test API ###################################################
#############################################################################################
@app.route("/predict_charges")
def get_insurance_charges():
    input_data = request.form

    age = int(input_data["age"])  # srting to int
    sex = input_data["sex"]   # string ch paheje
    bmi = int(input_data["bmi"])
    children = eval(input_data["children"])
    smoker = input_data["smoker"]
    region = input_data["region"]
     
    med_ins = MedicalInsurance(age,sex,bmi,children,smoker,region)
    charges = med_ins.get_predict_charges()
    return jsonify({"Return" : f"Predicted medical isurance charges are :{charges}"})
    
    



if __name__ == "__main__":
    app.run( )  # server start