from flask import Flask, render_template, jsonify, request, redirect, session, url_for, make_response
from datetime import datetime, timedelta
import secrets

@app.route("/")
def home():
    return render_template('home.html')