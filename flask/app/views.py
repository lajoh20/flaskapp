from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
from app import app
import os
from app.import_csv import import_csv
from datetime import datetime

ALLOWED_EXTENSIONS = set(['csv'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def index():
    return render_template("welcome.html")

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            new_filename = f'{filename.split(".")[0]}_{str(datetime.now())}.csv'
            save_location = ('./input')
            file.save(save_location)
        return redirect(url_for('download.html',new_filename))
    return render_template('upload.html')

    
@app.route("/download/<new_filename>")
def download_file(new_filename):
    return send_from_directory('./input', new_filename)
    
    