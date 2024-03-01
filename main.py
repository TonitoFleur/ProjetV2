from flask import Flask, render_template

app = Flask("test")

@app.route("/")
def index():
  return render_template("index.html")

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

app.run(host="0.0.0.0", port=80)
