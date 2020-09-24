from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def configure(app):
    db.init_app(app)
    app.db = db

class Harvest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    info = db.Column(db.String(255), nullable=False)
    date = db.Column(db.DateTime(), nullable=False)
    height = db.Column(db.Integer(), nullable=False)
    tree_id =  db.Column(db.Integer, db.ForeignKey('tree.id'), nullable=False)

    def __repr__(self):
        return '<Harvest %r>' % self.info