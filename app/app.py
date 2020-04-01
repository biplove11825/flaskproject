from flask import Flask,render_template,request,redirect
import csv

# Configure app
app = Flask(__name__)

#Registered students
students = []

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/registrants')
def registrants():
    with open("registered.csv", "r") as file:
        reader = csv.reader(file)
        students = list(reader)
    return render_template("registered.csv", students=students)


@app.route("/Register",methods=["POST"])
def register():
    name = request.form.get("name")
    hobbies = request.form.get("Hobbies")
    address = request.form.get("address")
    number = request.form.get("number")
    if not name or not hobbies or not address or not number:
        return render_template("failure.html")
    file = open("registered.csv", "a")
    writer = csv.writer(file)
    writer.writerow((request.form.get("name"),request.form.get("address"),request.form.get("number"),request.form.get("Hobbies")))
    file.close()
    return render_template("success.html")   
