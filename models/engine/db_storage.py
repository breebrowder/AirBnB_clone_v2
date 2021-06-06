#!/usr/bin/python3
""" Here we will create a new engine DBStorage """
from os import getenv
from sqlalchemy import create_engine

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
        # dialect+driver://username:password@host:port/database
        self.__engine = create_engine('mysql+mysql_db://{}:{}@{}:3306/{}'.
                                      format(user, passwd, host, db), pool_pre_ping=True)

    def all(self, cls=None):
        """query all the rows with given classes"""

        from models.amenity import Amenity
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State
        from models.user import User

        rows = []
        classes = [State, City, User, Place, Review, Amenity]
        if cls is None:
            for cls in classes:
                rows = rows + self.__session.query(cls)
        else:
            rows = self.__session.query(cls)
        return {type(row).__name__ + "." + row.id: row for row in rows}

    def new(self, obj):
        """ Add the object to the current database session """
        self.__session.add(obj)

    def save(self):
        """ Commit all changes of the current database session """
        self.__session.commit()

    def reload(self):
        """ Create all tables in the db, create the current session """
        from models.base_model import Base
        from sqlalchemy.orm import sessionmaker, scoped_session

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all()
        Base.metadata.create_all(self.__engine)
        # missing code here
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session1 = scoped_session(session_factory)
        self.__session = Session1()

    def delete(self, obj=None):
        """ Delete from the current database session obj if not None """
        if obj is not None:
            self.__session.delete(obj)
            self.save()

    def close(self):
        """session close"""
        self.__session.close()
