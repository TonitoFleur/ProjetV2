from flask import Flask, render_template, request, url_for, redirect, session

import pymongo

import os

import bcrypt

from bson.objectid import ObjectId

app = Flask("ecommerce")

mongo = pymongo.MongoClient(os.getenv("MONGO_DB"))
# BDD TEST

@app.route('/test')
def test():
  db_test = mongo.db.test
  test = db_test.find({})
  return render_template('test.html', test=test)
  
# Section BDD



# Fin Section BDD

@app.route("/")
def index():
  return render_template("accueil.html")
  
@app.route("/login")
def login():
  return render_template("login.html")

@app.route('/register')
def register():
  return render_template("register.html")

@app.route('/contact')
def contact():
  return render_template("contact.html")

@app.route('/sneakers')
def sneakers():
  return render_template("sneakers.html")

@app.route('/phones')
def phones():
  return render_template("phones.html")

@app.route('/clothes')
def clothes():
  return render_template("clothes.html")

app.run(host="0.0.0.0", port=81)
