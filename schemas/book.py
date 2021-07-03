from ma import marshmallow
from models.book import BookModel


class BookSchema(marshmallow.SQLAlchemyAutoSchema):
    
    class Meta:
        model = BookModel
        load_instance = True
        