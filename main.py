from flask import Flask, render_template, request, url_for, redirect, session

#import pymongo pour l'utiliser dans replit
import pymongo

# import de sécurité
import os

# pour crypter les mots de passe
import bcrypt

# Pour gérer les ObjectId
from bson.objectid import ObjectId

app = Flask("ecommerce")
# Début de mon code

#Connexion a la bdd
mongo = pymongo.MongoClient(os.getenv("AMAZONITE_DB"))

# Cookie de la session utilisateur
app.secret_key = os.getenv("COOKIES_KEY")

# BDD TEST


@app.route('/test')
def test():
  db_test = mongo.db.test
  test = db_test.find({})
  return render_template('test.html', test=test)


# Section BDD

# Fin Section BDD


@app.route("/")
def accueil():
  return render_template("accueil.html")


@app.route('/login', methods=['POST', 'GET'])
def login():
  if request.method == 'POST':
    db_utils = mongo.db.utilisateurs
    util = db_utils.find_one({'nom': request.form['utilisateur']})
    if util:
      if bcrypt.checkpw(request.form['mot_de_passe'].encode('utf-8'),
                        util['mdp']):
        session['util'] = request.form['utilisateur']
        return redirect(url_for('accueil'))
      else:
        return render_template('login.html', erreur="Mauvais mdp")
    else:
      return render_template('login.html', erreur="Mauvais utilisateur")
  else:
    return render_template('login.html')


@app.route('/logout')
def logout():
  session.clear()
  return redirect(url_for('accueil'))


@app.route('/register', methods=['POST', 'GET'])
def register():
  if request.method == 'POST':
    db_utils = mongo.db.utilisateurs
    if (db_utils.find_one({'nom': request.form['utilisateur']})):
      return render_template('register.html',
                             erreur="Le nom d'utilisateur existe deja")
    else:
      if (request.form['mot_de_passe'] == request.form['verif_mot_de_passe']):
        mdp_encrypte = bcrypt.hashpw(
            request.form['mot_de_passe'].encode('utf-8'), bcrypt.gensalt())
        db_utils.insert_one({
            'nom': request.form['utilisateur'],
            'mdp': mdp_encrypte,
            'mail': request.form['mail'],
            'role': "abonné"
        })
        session['util'] = request.form['utilisateur']
        return redirect(url_for('accueil'))
      else:
        return render_template("register.html")
  else:
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


@app.route("/annonce")
def annonce():
  return render_template("annonce.html")


# admin


@app.route('/admin/sneakers')
def admin_sneakers():
  return render_template("/admin/sneakers.html")


@app.route('/admin/clothes')
def admin_clothes():
  return render_template("/admin/clothes.html")


app.run(host="0.0.0.0", port=81)
