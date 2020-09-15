from flask import render_template

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
 
 def NormaliseGenreScore(self):
	 score_sum = 0
	for _,value in self.genre.items():
		score_sum = score_sum+value
	for key,value in self.genre.items():
		self.genre[key] = (value/score_sum)*len(self.genre)*100

 def Serialize(self):
  return ((self.time,self.author,self.poster,self.review,self.tlink,self.trailer,self.dd_link,self.name)+
          tuple((self.genre[genre_name] for genre_name in self.genre_list)))


 def __repr__(self):
  return '\n'.join(f'{key}:{value}' for key,value in self.__dict__.items())


class MoviePage:
	ppp = None
	db = None
	template_name = None
	cache = {}
	def __init__(self,page_no):
		self.page_no = page_no
		self.startIdx = (page_no-1)*self.ppp+1
		self.EndIdx = self.startIdx+self.ppp-1 if (self.startIdx+self.ppp-1 <=self.db.NofPosts) else self.db.NofPosts
		self.valid = None
		self._posts = []
		self.template = None

	def InitMoviePage(cls,posts_per_page,db,template_name):
		cls.ppp = posts_per_page
		cls.db = db
		cls.template_name = template_name

	def RenderMoviePage(page_no):
		if page_no in self.cache.keys():
			return self.cache[page_no]
		else:
			posts = self.posts
			if posts:
				self.template = render_template(self.template_name,movies=posts)
			else:
				self.template = "<h1> Invalid Page </h1>"
			self.cache[page_no] = self.template
			return self.template
	
	@property
	def posts(self):
		for i in range(self.startIdx,self.EndIdx+1):
			post = self.db.getMovieByID(i)
			if post:
				self._posts.append(post)
			else:
				return self._posts
		return self._posts

	



		