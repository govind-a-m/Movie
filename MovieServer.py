from flask import Flask,render_template,request,session,jsonify

app = Flask(__name__)
app.secret_key = 'szPnSXYHxNkMKDUEE6FbYfCM'

@app.route("/",methods=['GET','POST'])
def home():
  if request.method == 'POST':
    return jsonify(request.form.to_dict())
  else:
    return render_template('horizontal_cards.html')


if __name__=="__main__":
  app.run(debug=True)