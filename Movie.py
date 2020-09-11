

class movie:
 genre_list = ['r_docu','r_sci','r_mys','r_thr','r_act','r_phi','r_com','r_min','r_exp']
 def __init__(self,time,author,poster,review,tlink,trailer,dd_link,name,genre,idx=None):
  self.idx = idx
  self.name = name
  self.author = author
  self.time = time
  self.tlink = tlink
  self.poster = poster
  self.genre = genre
  self.review = review
  self.trailer = trailer
  self.dd_link = dd_link

 def Serialize(self):
  return ((self.time,self.author,self.poster,self.review,self.tlink,self.trailer,self.dd_link,self.name)+
          tuple((self.genre[genre_name] for genre_name in self.genre_list)))


 def __repr__(self):
  return '\n'.join(f'{key}:{value}' for key,value in self.__dict__.items())

