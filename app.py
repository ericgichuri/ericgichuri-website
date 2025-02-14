from flask import Flask,render_template, redirect,url_for,jsonify
import os, time

app=Flask(__name__)

@app.route("/")
@app.route("/home")
def func_home():
    return render_template("index.html")

@app.route("/projects")
def func_projects():
    return render_template("projects.html")

@app.route("/project",defaults={"slug":None})
@app.route("/project/<slug>")
def func_project():
    return render_template("project.html")

@app.route("/contact")
def func_contact():
    return render_template("contact.html")

@app.route("/services")
def func_services():
    return render_template("services.html")

if __name__=="__main__":
    app.run(debug=True)