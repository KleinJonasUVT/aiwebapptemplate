from flask import Flask, render_template, jsonify, request, redirect, session, url_for, make_response
from datetime import datetime, timedelta
import secrets

@app.route("/")
def home():
    return render_template('home.html')

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)