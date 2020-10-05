from passlib.hash import sha256_crypt
import json

class User:
  db = None
  Active = {}

  def __init__(self,name,pwd,Liked=''):
    self.name = name
    self.pwd = pwd
    self.Liked = Liked

  @classmethod
  def Init(cls,db):
    cls.db = db
  
  def VerifyUser(self):
    rsp = self.db.GetUserByName(self.name)
    if rsp:
      pwd_hash = rsp['password']
      liked_txt = rsp['Liked']
      if sha256_crypt.verify(self.pwd,pwd_hash):
        self.Liked = liked_txt
        self.__class__.Active[self.name] = self.Liked
        return "SUCCESS"
      else:
        return "WRONG_PWD"
    else:
      return "UNKNOWN_USER"
  
  def AddUser(self):
    if len(self.name)>0:
      if len(self.pwd)>0:
        self.pwd = sha256_crypt.hash(self.pwd)
        self.db.AddUser(self)
        return "SUCCESS"
      else:
        return "PWD_SHORT"
    else:
      return "USERNAME_SHORT"
  
  @classmethod
  def GetUserByName(cls,name):
    pwd = cls.db.GetUserByName(name)
    if pwd:
      return cls(name,pwd)
    else:
      return None

  @classmethod
  def DelUser(cls,name):
    cls.db.DelUser(name)

  @staticmethod
  def ConvToList(text):
    return json.loads(text)

  @staticmethod
  def ConvToText(liked_li):
    return json.dumps(liked_li)

  @classmethod
  def AddLiked(cls,name,mv_name):
    if name in cls.Active:
      if cls.Active[name].find(mv_name)==-1:
        cls.Active[name] = cls.Active[name] + "," + mv_name
        cls.db.UpdateLiked(name,cls.Active[name])
        cls.db.IncreaseLikeCount(mv_name)
        return 'SUCCESS'
      else:
        return "ALREDY_LIKED"
    else:
      return "UNKNOWN_USER"

  @classmethod
  def RemoveLiked(cls,name,mv_name):
    if name in cls.Active:
      if cls.Active[name].find(mv_name)!=-1:
        cls.Active[name] = cls.Active[name].replace(mv_name,'')
        cls.db.UpdateLiked(name,cls.Active[name])
        cls.db.DecreaseLikeCount(mv_name)
        return 'SUCCESS'
      else:
        return 'MOVIE_NOT_FOUND'
    else:
      return 'UNKNOWN_USER'

  @classmethod
  def CheckIfLiked(cls,username,mv_name):
    if username in cls.Active:
      if cls.Active[username].find(mv_name)==-1:
        return False
      else:
        return True
    else:
      return None

  def __repr__(self):
    return f'{self.name},{self.pwd},{self.Liked}'


if __name__=="__main__":
  from AccessDB import DataBase
  db = DataBase()
  username = 'Jonas_Kahnwald'
  password = 'samayatalme'
  User.Init(db)
  print(User(username, password).VerifyUser())
  print(User.Active)
  mv_name = 'Dark Waters'
  print(User.CheckIfLiked(username,mv_name))
  print(User.RemoveLiked(username,mv_name))
  print(User.db.QueryLikeCount(mv_name))
  print(User.Active)
  User.db.close()
  # print(User.GetUserByName(username))

  # User.DelUser(username)
  # print(User.GetUserByName(username))
  # User(username,password).AddUser()
  # print(User.GetUserByName(username))
  # print(User(username,password).VerifyUser())
