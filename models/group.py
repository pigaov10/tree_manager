from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def configure(app):
    db.init_app(app)
    app.db = db

class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    age = db.Column(db.Integer(), nullable=False)
    tree_id =  db.Column(db.Integer, db.ForeignKey('tree.id'), nullable=False)

    def __repr__(self):
        return '<Group %r>' % self.description