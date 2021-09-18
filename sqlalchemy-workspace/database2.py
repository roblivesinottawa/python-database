from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine("mysql+mysqlconnector://root:mysqlpassmacrob@localhost:3306/comics", echo=True)

Base = declarative_base()

class ComicBookProject(Base):
	__tablename__ = 'comic_books_projects'
	__table_args__ = {'schema':'comics'}

	project_id = Column(Integer, primary_key=True)
	title = Column(String(length=50))
	description = Column(String(length=50))

	def __repr__(self):
		return f"<ComicBookProject(title'{self.title}', description='{self.description})'>"

class MarvelBook(Base):
	__tablename__ = 'marvel_books'
	__table_args__ = {'schema':'comics'}

	marvel_id = Column(Integer, primary_key=True)
	project_id = Column(Integer, ForeignKey('comics.comic_books_projects.project_id'))
	description = Column(String(length=50))

	project = relationship("ComicBookProject")

	def __repr__(self):
		return f"<MarvelBook(description='{self.description})'>"

Base.metadata.create_all(engine)

# create a session to query database
session_maker = sessionmaker()
# bind the session to the engine
session_maker.configure(bind=engine)
session = session_maker()

# transaction: all queries are either successful or not

organize_comics_project = ComicBookProject(
    title='Organize comics', 
	description='Organize comic books by year of release')
    # to insert into the database
session.add(organize_comics_project)
session.commit() # so as to initialize the next task transactions

# add some marvel books
marvel_books = [
    MarvelBook(
    project_id=organize_comics_project.project_id, 
    description='The Invincible Iron Man: The Five Nightmares'),
    MarvelBook(
    project_id=organize_comics_project.project_id, 
    description='Thunderbolts: Cage'),
    MarvelBook(
    project_id=organize_comics_project.project_id, 
    description='Astonishing X-Men: Xenogenesis'),
]

# to put books in the database
session.bulk_save_objects(marvel_books)
session.commit()

# query database to retrieve info
my_project = session.query(ComicBookProject).filter_by(title='Organize comics').first()
print(my_project)

# retrieve all marvel books
my_marvel_books = session.query(MarvelBook).all()
print(my_marvel_books)