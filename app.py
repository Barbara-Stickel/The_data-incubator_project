import os
import sys
from flask import Flask, request, session, g, redirect, url_for, abort, render_template

app = Flask(__name__)

@app.route("/")
def home():
	return render_template('layout.html')

if __name__ == '__main__':
   app.run() #debug=True