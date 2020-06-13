from flask import render_template, session, request, redirect, url_for, flash, send_from_directory
from bootstrap import app, cache


@app.route('/')
@app.route('/home')
def index():
    return render_template('home/index.html')
