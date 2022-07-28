from flask import Flask, render_template, request, redirect, url_for
from app import app
import os
from app.import_csv import import_csv

@app.route("/")
def index():
    return render_template("main.html")

@app.route("/upload", methods= ['GET',"POST"] )
def upload():
    if request.method == 'POST':
        pass
    return render_template("upload.html")

