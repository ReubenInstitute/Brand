from flask import Flask
from flask import send_file
from flask import send_from_directory
from flask import abort
import subprocess
import shutil
import os
import Paths

CSS_FOLDER = Paths.CSS_FOLDER
FONT_FOLDER = Paths.FONT_FOLDER
if os.environ.get('CSS_FOLDER'):
	CSS_FOLDER = os.environ.get('CSS_FOLDER')
if os.environ.get('FONT_FOLDER'):
	FONT_FOLDER = os.environ.get('FONT_FOLDER')

app = Flask(__name__)

@app.route('/')
def index():
	return send_file('test.html')

@app.route(f'{Paths.CSS_URL}/<filename>.css')
def serve_css_file(filename):
	return send_from_directory(CSS_FOLDER, f'{filename}.css')

@app.route(f'{Paths.FONT_URL}/<path:filename>.ttf')
@app.route(f'{Paths.FONT_URL}/<path:filename>.otf')
@app.route(f'{Paths.FONT_URL}/<path:filename>.woff2')
def serve_font_file(filename):
	return send_from_directory(FONT_FOLDER, filename)

if __name__ == '__main__':
	app.run(host='127.0.0.1', port=5000, debug=True)