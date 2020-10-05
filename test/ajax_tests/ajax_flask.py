from flask import Flask, render_template, request, json

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/signUp')
def signUp():
    return render_template('signUp.html')

if __name__=="__main__":
    app.run()