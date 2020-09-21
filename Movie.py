from flask import render_template
from datetime import datetime
from werkzeug.utils import secure_filename
import os


class movie:
	genre_list = ['r_doc','r_sci','r_mys','r_thr','r_act','r_phi','r_com','r_min','r_exp']
	db = None
	config = None
	page = None
	def __init__(self,author,poster,review,tlink,trailer,dd_link,name,genre,idx=None,time=datetime.now().strftime("%d/%m/%Y %H:%M:%S")):
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
	
	@classmethod
	def Initmovie(cls,db,config,page):
		cls.db = db
		cls.config = config
		cls.Page = page

	def NormaliseGenreScore(self):
		score_sum = 0
		for _,value in self.genre.items():
			score_sum = score_sum+value
		for key,value in self.genre.items():
			self.genre[key] = (value/score_sum)*len(self.genre)*100

	def Serialize(self):
		print(self.genre,self.genre_list)
		return ((self.idx,self.time,self.author,self.poster,self.review,self.tlink,self.trailer,self.dd_link,self.name)+
						tuple((self.genre[genre_name] for genre_name in self.genre_list)))
	
	@classmethod
	def addMovie(cls,request):
		genres = {}
		cls.Page.ClearCache()
		form = request.form
		for genre in cls.genre_list:
			genres[genre] = form[genre] 
		poster_name = cls.SaveImage(request.files)
		mv = cls(form['UserName'],poster_name,form['review'],form['torrent_link'],form['trailer_link'],form['dd_link'],form['MovieName'],genres,idx=cls.db.NofPosts()+1)
		cls.db.AddPost(mv)

	@classmethod
	def DeleteMovieById(cls,id):
		idx = int(id)
		page_no = cls.Page.GetPageId(idx)
		if page_no:
			cls.Page.ClearCacheFrom(page_no)
			cls.db.DelPostByID(idx)
			return True
		else:
			return False
		
	@classmethod
	def SaveImage(cls,files):
		try:
			filename = secure_filename(files['poster'].filename)
			files['poster'].save(os.path.join(cls.config['UPLOAD_FOLDER'],filename))
			return os.path.join(r"/static/posters",filename)
		except:
			print('no poster')
			return r'/static/posters/blank_poster.jpg'

	def __repr__(self):
		return '\n'.join(f'{key}:{value}' for key,value in self.__dict__.items())


class MoviePage:
	ppp = None
	db = None
	template_name = None
	cache = {}
	
	def __init__(self,page_no):
		self.page_no = page_no
		nofposts = self.db.NofPosts()
		self.startIdx = nofposts-((page_no-1)*self.ppp)
		self.EndIdx = 1 if (self.startIdx-self.ppp+1 <=0) else self.startIdx-self.ppp+1
		self.valid = None
		self.posts = []
		self.template = None
	
	@classmethod
	def InitMoviePage(cls,posts_per_page,db,template_name):
		cls.ppp = posts_per_page
		cls.db = db
		cls.template_name = template_name

	@classmethod
	def RenderMoviePage(cls,page_no):
		print('cache',cls.cache.keys())
		if page_no in cls.cache.keys():
			return cls.cache[page_no]
		else:
			page = cls(page_no)
			page.Getposts()
			page.template = render_template(cls.template_name,movies=page.posts)
			cls.cache[page_no] = page.template
			return page.template
	
	def Getposts(self):
		for i in range(self.startIdx,self.EndIdx-1,-1):
			print(i)
			post = self.db.getMovieByID(i)
			if post:
				self.posts.append(post)
			else:
				print(f'no post with id{i}')
				return self.posts
		return self.posts

	@classmethod
	def ClearCacheFrom(cls,page_no):
		keys = list(cls.cache.keys())
		for key in keys:
			if key>=page_no:
				del cls.cache[key]

	@classmethod
	def ClearCache(cls):
		cls.cache = {}
	
	@classmethod 
	def GetPageId(cls,m_idx):
		m_idx = cls.db.NofPosts()-m_idx+1
		page_no = (m_idx//cls.ppp)+(m_idx%cls.ppp)
		return page_no

	def isinpage(self,movie_idx):
		m_idx = selm_idx
		if (self.startIdx<=movie_idx) and (movie_idx<=self.EndIdx):
			return True
		else:
			return False


	



		