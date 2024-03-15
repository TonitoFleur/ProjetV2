from flask import Flask, render_template, request, url_for, redirect, session

#import pymongo pour l'utiliser dans replit
import pymongo

# import de sécurité 
import os

# pour crypter les mots de passe
import bcrypt

# Pour gérer les ObjectId 
from bson.objectid import ObjectId

app = Flask("Mon Site")
# Début de mon code

#Connexion a la bdd 
mongo = pymongo.MongoClient(os.getenv("AMAZONITE_DB"))

# Cookie de la session utilisateur 
#app.secret_key = os.getenv("COOKIES_KEY")
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
