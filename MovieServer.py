
from flask import Flask,render_template,request,session,jsonify
from Movie import MoviePage,movie
from AccessDB import DataBase

app = Flask(__name__)
app.secret_key = 'szPnSXYHxNkMKDUEE6FbYfCM'
app.config['UPLOAD_FOLDER'] = r'C:\Users\govin\Documents\Movie\static\posters'
db = DataBase()
MoviePage.InitMoviePage(2,db,'MoviePage.html')
movie.Initmovie(db,app.config,MoviePage)

@app.route("/",methods=['GET'])
def login():
  return render_template('index.html')
# def home():
#   if request.method == 'POST':
#     if request.form['action']=='add':
#       movie.addMovie(request)
#       return MoviePage.RenderMoviePage(1)
#     elif request.form['action'] == 'delete':
#       movie.DeleteMovieById(request.form['MovieId'])
#       return MoviePage.RenderMoviePage(1)
#     else:
#       return jsonify(request.form.to_dict(flat=False))
#   else:
#     return MoviePage.RenderMoviePage(1)


if __name__=="__main__":
  app.run(host='0.0.0.0')

