import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from werkzeug import secure_filename

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(
	DATABASE = os.path.join(app.root_path, 'flaskr.db'),
	SECRET_KEY='Anonymous',
	USERNAME='root',
	PASSWORD='root'
	))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

UPLOAD_FOLDER = 'images'
#ALLOWED_EXTENSION = set(['png', 'jpg', 'jpeg', 'bmp'])

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/auth', methods=['GET', 'POST'])
def authenticate():
	if request.method == 'POST':
		f = request.files['image']
		filename = secure_filename(f.filename)
		f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		return "File name: "+os.path.join(app.config['UPLOAD_FOLDER'], f.filename)
	else:
		return "Not successful"
