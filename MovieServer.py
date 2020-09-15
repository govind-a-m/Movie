
from flask import Flask,render_template,request,session,jsonify
from Movie import MoviePage
from AccessDB import DB

app = Flask(__name__)
app.secret_key = 'szPnSXYHxNkMKDUEE6FbYfCM'
db = DB()
MoviePage.InitMoviePage(2,db,'MoviePage.html')

@app.route("/",methods=['GET','POST'])
def home():
  if request.method == 'POST':
    return jsonify(request.form.to_dict())
  else:
    return MoviePage.RenderMoviePage(1)


if __name__=="__main__":
  app.run(debug=True)