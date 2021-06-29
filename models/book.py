from db import db


class BookModel(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False, unique=True)
    pages = db.Column(db.Integer, nullable=False)

    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __repr__(self, ):
        return f'BookModel(title={self.title}, pages={self.pages})'

    def json(self, ):
        return {
            'title': self.title,
            'pages': self.pages
        }
