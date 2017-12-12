from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'postgres://onjbqxeeaaysxv:39b665c3775984732b26fa04e72161bc7bc31fdc22d62f2762d85a02486ee8eb@ec2-23-21-220-48.compute-1.amazonaws.com:5432/dcb970e2t38qli'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


class UserData(db.Model):
    __tablename__ = 'UserData'

    Id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(64))
    Description = db.Column(db.String(256))
    CreateDate = db.Column(db.DateTime)

    def __init__(self
                 , Name
                 , Description
                 , CreateDate
                 ):
        self.Name = Name
        self.Description = Description
        self.CreateDate = CreateDate


if __name__ == '__main__':
    manager.run()
