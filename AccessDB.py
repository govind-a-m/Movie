import sqlite3
from Movie import movie

class DataBase:
 def __init__(self):
   self.conn = sqlite3.connect(r'C:\Users\govin\Documents\Movie\MovieData.db',check_same_thread=False)
   self.conn.row_factory = sqlite3.Row
   self.c = self.conn.cursor()
 
 def NofPosts(self):
   self.c.execute("SELECT MAX(idx) FROM posts")
   nofrows = self.c.fetchone()
   if nofrows[0]:
     return nofrows[0]
   else:
     return 0

 def AddPost(self,movie):
   self.c.execute('''INSERT INTO posts (idx,time,author,poster,review,tlink,trailer,dd_link,
                  name,r_doc,r_sci,r_mys,r_thr,r_act,r_phi,r_com,r_min,r_exp)
                  VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',movie.Serialize())
   self.conn.commit()

 def DelPostByName(self,movie_name):
   self.c.execute('DELETE FROM posts WHERE name=?',(movie_name,))
   self.conn.commit()

 def DelPostByID(self,idx):
   self.c.execute('DELETE FROM posts WHERE idx=?',(idx,))
   self.c.execute('UPDATE posts SET idx=idx-1 WHERE idx>?',(idx,))
   self.conn.commit()

 def DelAllPosts(self):
   self.c.execute('DELETE FROM posts')
   self.conn.commit()

 def getMovieByname(self,name):
   self.c.execute('SELECT * FROM posts WHERE name=?',(name,))
   rsp = self.c.fetchone()
   if rsp:
     mv = movie(rsp['author'],rsp['poster'],rsp['review'],
                rsp['tlink'],rsp['trailer'],rsp['dd_link'],rsp['name'],
                self.getGenre(rsp),idx=rsp['idx'],time=rsp['time'])
     return mv
   else:
     return None

 def getMovieByID(self,idx):
   self.c.execute('SELECT * FROM posts WHERE idx=?',(idx,))
   rsp = self.c.fetchone()
   if rsp:
     mv = movie(rsp['author'],rsp['poster'],rsp['review'],
          rsp['tlink'],rsp['trailer'],rsp['dd_link'],rsp['name'],self.getGenre(rsp),idx=rsp['idx'],time=rsp['time'])
     return mv
   else:
     return None

 def close(self):
   self.conn.commit()
   self.conn.close()

 @staticmethod
 def getGenre(rsp):
   gnrs = {}
   for gnr in movie.genre_list:
     gnrs[gnr] = rsp[gnr]
   return gnrs


 @classmethod
 def CreateDb(cls):
   conn = sqlite3.connect('MovieData.db')
   c = conn.cursor()
   c.execute('''CREATE TABLE posts
           (idx INTEGER PRIMARY KEY AUTOINCREMENT,
            time text,author text,poster text,review text,
            tlink text,trailer text,dd_link text,name text,
            r_doc real,r_sci real, r_mys real,r_thr real,
            r_act real,r_phi real,r_com real,r_min real,r_exp real)''')
   conn.commit()
   c.close()
   conn.close()


if __name__ == '__main__':
 DataBase.CreateDb()
 db = DataBase()
 m = movie(name='name',
           author='author',
           time = 'time',
           tlink = 'tlink',
           poster = 'poster',
           genre = {'r_doc':'r_doc','r_sci':'r_sci','r_mys':'r_mys','r_thr':'r_thr','r_act':'r_act','r_phi':'r_phi','r_com':'r_com','r_min':'r_min','r_exp':'r_exp'},
           review = 'review',
           trailer = 'trailer',
           dd_link = 'dd_link')
 db.AddPost(m)
 db.AddPost(m)
 db.AddPost(m)
 print(db.getMovieByname('name'))
 print(db.getMovieByID(1))
 db.close()






