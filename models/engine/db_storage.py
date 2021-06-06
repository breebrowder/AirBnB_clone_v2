#!/usr/bin/python3
""" Here we will create a new engine DBStorage """
""" Private class attributes: __engine and __session """
""" Public instance methods: __init__(self), all(self, cls=None) """
""" Cont. new(self, obj), save(self), delete(self, obj=None) """
""" Cont. reload(self) """


class DBStorage():
   """ Class for new engine DBStorage """
   __engine = None
   __session = None

   def __init__(self):
       user = getenv('HBNB_MYSQL_USER')
       passwd = getenv('HBNB_MYSQL_PWD')
       host = getenv('HBNB_MYSQL_HOST')
       db = getenv('HBNB_MYSQL_DB')
       self.__engine = create_engine(
          # missing code here that adds pool_pre_ping=True option when we call create_engine
      if getenv('HBNB_ENV') == 'test':
          Base.metadata.drop_all(self.__engine)

   def new(self, obj):
          """ Add the object to the current database session """
          self.__session.add(obj)

   def save(self):
          """ Commit all changes of the current database session """
          self.__session.commit()

   def reload(self):
          """ Create all tables in the db, create the current session """
          Base.metadata.create_all(self.__engine)
          # missing code here

   def delete(self, obj=None):
          """ Delete from the current database session obj if not None """
          if obj is not None:
          self.__session.delete(obj)
