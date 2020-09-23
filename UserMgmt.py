from passlib.hash import sha256_crypt


class User:
  db = None

  def __init__(self,name,pwd):
    self.name = name
    self.pwd = pwd
  
  @classmethod
  def Init(cls,db):
    cls.db = db
  
  def VerifyUser(self):
    user = self.db.GetUserByName(self.name)
    if user:
      if(sha256_crypt.verify(self.pwd,user.pwd)):
        return "WRONG_PWD"
      else:
        return "SUCCESS"
    else:
      return "UNKNOWN_USER"
  
  def AddUser(self):
    if len(self.name)>0:
      if len(self.pwd)>0:
        self.pwd = sha256_crypt.encrypt(self.pwd)
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
  
  def __repr__(self):
    return f'{self.name},{self.pwd}'
