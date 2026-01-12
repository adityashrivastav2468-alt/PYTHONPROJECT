from flask import Flask,render_template

app= Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html',name= 'I am Aditya')
@app.route("/about")
def about():
    return 'I am Aditya.'
@app.route("/contact")
def contact():
    return render_template('contact.html')