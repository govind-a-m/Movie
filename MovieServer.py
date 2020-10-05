
from flask import Flask,render_template,request,session,jsonify,flash,json
from Movie import MoviePage,movie
from AccessDB import DataBase
from UserMgmt import User


app = Flask(__name__)
app.secret_key = 'szPnSXYHxNkMKDUEE6FbYfCM'
app.config['UPLOAD_FOLDER'] = r'.\static\posters'
db = DataBase()
MoviePage.InitMoviePage(2,db,'MoviePage.html')
movie.Initmovie(db,app.config,MoviePage)
User.Init(db)

@app.route("/",methods=['GET'])
def index():
  return render_template('index.html')

@app.route("/Movies/<int:page_no>",methods=['GET','POST'])
def MoviePageRequest(page_no):
  if 'logged_in' in session:
    if request.method=='GET':
      return MoviePage.RenderMoviePage(page_no)
    else:
      return ProcessMovieForm(request,page_no,session['username'])
  else:
    return "<h1> not logged in </h1>"


@app.route("/ajaxlogin",methods=['POST'])
def ajaxlogin():
  if request.form['username']:
    if request.form['password']:
      if User(request.form['username'],request.form['password']).VerifyUser()=='SUCCESS':
        session['logged_in'] = True
        session['username'] =request.form['username']
        return json.dumps({'status': 'OK', 'login':'SUCCESS'});
  return json.dumps({'status': 'OK', 'login': 'FAIL'});

@app.route("/Likes",methods=['POST'])
def RegisterLikes():
  # required as space is replaced with + form.serialize
  movie_name = DecodeMovieName(request.form['movie_name'])
  if 'logged_in' in session:
    if movie_name:
      if request.form['Like']=='like':
        if User.CheckIfLiked(session['username'],movie_name):
          return json.dumps({'status':'OK','OP_STAT':'ALREADY_LIKED','movie_name':movie_name})
        else:
          if User.AddLiked(session['username'],movie_name)=='SUCCESS':
            nof_likes = movie.QueryLikeCount(movie_name)
            return json.dumps({'status': 'OK', 'OP_STAT': 'ADDED_TO_LIKED','LikeCount':nof_likes})
      elif request.form['Like'] == 'unlike':
        if User.CheckIfLiked(session['username'],movie_name):
          if User.RemoveLiked(session['username'],movie_name)=='SUCCESS':
            nof_likes = movie.QueryLikeCount(movie_name)
            return json.dumps({'status': 'OK', 'OP_STAT': 'REMOVED_FROM_LIKED','LikeCount':nof_likes})
          else:
            print('unlike not succesfull')
  return json.dumps({'status': 'OK', 'OP_STAT': 'ERROR'})

@app.route("/LikeQuery",methods=['POST'])
def QueryLikeStatus():
  if 'logged_in' in session:
    if request.form['movie_name']:
      nof_likes = movie.QueryLikeCount(request.form['movie_name'])
      if User.CheckIfLiked(session['username'],request.form['movie_name']):
        return json.dumps({'status':'OK','Liked':'YES','LikeCount':nof_likes})
      else:
        return json.dumps({'status':'OK','Liked':'NO','LikeCount':nof_likes})
  return json.dumps({'status': 'OK', 'Liked': 'NULL'})


@app.route("/UsernameQuery",methods=['GET'])
def QueryUsername():
  if 'logged_in' in session:
    return json.dumps({'status':'OK','UserName':session['username']})


def DecodeMovieName(movie_name):
  ret = movie_name.replace('+',' ');
  return ret

def ProcessMovieForm(request,page_no,username):
  if request.form['action'] == 'add':
    movie.addMovie(request,username)
    return MoviePage.RenderMoviePage(1)
  elif request.form['action'] == 'delete':
    movie.DeleteMovieById(request.form['MovieId'])
    return MoviePage.RenderMoviePage(page_no)
  else:
    return "<h1> invalid operation </h1>"

if __name__=="__main__":
  app.run(debug=True)



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

# @app.route("/",methods=['POST'])
# def login():
#   if request.form['username']:
#     if request.form['password']:
#       if User(request.form['username'],request.form['password']).VerifyUser()=='SUCCESS':
#         'logged_in' in session = True
#         flash('you were succesfully logged in')
#         return MoviePage.RenderMoviePage(1)
#       else:
#         flash('wrong password or username')
#   return render_template('index.html')