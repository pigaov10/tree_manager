from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def configure(app):
    db.init_app(app)
    app.db = db

class Tree(db.Model):
    __tablename__ = 'tree'
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    age = db.Column(db.Integer(), nullable=False)
    # specie_id =  db.Column(db.Integer, db.ForeignKey('specie.id'), nullable=False)

    def __repr__(self):
        return '<Tree %r>' % self.description