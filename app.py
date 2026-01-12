from flask import Flask

app= Flask(__name__)

@app.route("/")
def index():
    return render_templates('index.html',name= 'I am Aditya')
@app.route("/about")
def about():
    return 'I am Aditya.'