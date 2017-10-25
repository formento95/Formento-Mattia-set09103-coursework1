from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

@app.route("/home/")
def home():
  return render_template('home.html'), 200

@app.route("/guitars/")
def guitars():
  return render_template('guitar.html'), 200

@app.route("/basses/")
def basses():
  return render_template('bass.html'), 200

@app.route("/")
def blank():
  return redirect(url_for('home'))

@app.route("/home/home")
def twohomes():
  return redirect(url_for('home'))

@app.route("/home/guitars")
def homeandguitars():
  return redirect(url_for('guitars'))

@app.route("/home/basses/")
def homeandbasses():
  return redirect(url_for('basses'))

@app.route("/basses/home")
def bassandhome():
  return redirect(url_for('home'))

@app.route("/guitars/home")
def guitarsandhome():
  return redirect(url_for('home'))

@app.route("/guitars/guitars")
def twoguitars():
  return redirect(url_for('guitars'))

@app.route("/guitars/basses")
def guitarandbase():
  return redirect(url_for('basses'))

@app.route("/basses/guitars")
def bassandguitar():
  return redirect(url_for('guitars'))

@app.route("/basses/basses")
def twobasses():
  return redirect(url_for('basses'))


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
