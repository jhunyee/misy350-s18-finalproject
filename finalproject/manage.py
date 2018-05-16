from flask_script import Manager
from moviebase import app, db, Director, Movie

manager = Manager(app)


# reset the database and create some initial data
@manager.command
def deploy():
    db.drop_all()
    db.create_all()

    wesanderson = Director(name="Wes Anderson", about="Wes Anderson is 49 years old")
    davidfincher = Director(name="David Fincher", about="David Fincher is 55 years old")
    quentintarantino = Director(name="Quentin Tarantino", about="Quentin Tarantino is 55 years old")
    movie1 = Movie(name="The Grand Budapest Hotel", year = 2014, director=wesanderson)
    movie2 = Movie(name="The Social Network", year = 2010, director=davidfincher)
    movie3 = Movie(name="Isle of Dogs", year = 2017, director=wesanderson)
    movie4 = Movie(name="Inglorious Basterds", year = 2009, director=quentintarantino)


    db.session.add(wesanderson)
    db.session.add(davidfincher)
    db.session.add(quentintarantino)
    db.session.add(movie1)
    db.session.add(movie2)
    db.session.add(movie3)
    db.session.add(movie4)
    db.session.commit()


if __name__ == "__main__":
    manager.run()
