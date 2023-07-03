from flask import *
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'
db=SQLAlchemy(app)



class Book(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    book_name = db.Column(db.String(80),unique=True,nullable=False)
    book_author = db.Column(db.String(80),nullable=False)
    book_publisher = db.Column(db.String(80),nullable=False)

    def __repr__(self):
        return f"Name: {self.book_name} - Author: {self.book_author} - Publisher: {self.book_publisher}"

#with app.app_context():
    #book = Book(book_name="Dune",book_author=("Frank Herbert"),book_publisher="Unknown")

    #book2 = Book(book_name="Hyperion",book_author=("Dan Simmons"),book_publisher="Has an S logo")

    #db.session.add(book)
    #db.session.add(book2)
    #db.session.commit()
@app.route('/')
def index():
    return 'Hello'

@app.route('/books')
def get_books():
    books = Book.query.all()
    output = []
    for book in books:
        book_data={'name':book.book_name,"author":book.book_author,"publisher":book.book_publisher}
        output.append(book_data)
    return {"drinks":output}

@app.route('/books/<id>')
def get_book(id):
    book = Book.query.get_or_404(id)
    return {'name':book.book_name,"author":book.book_author,"publisher":book.book_publisher}

@app.route('/drinks',methods=['POST'])
def add_book():
    book = Book(book_name=request.json['book_name'],book_author=request.json['book_author'],book_publisher=request.json['book_publisher'])
    db.session.add(book)
    db.session.commit
    return {"id":book.id}

@app.route('/drinks/<id>',methods=['DELETE'])
def delete_book(id):
    book = Book.query.get(id)
    if book is None:
        return {"error":"not found"}
    db.session.delete(book)
    db.session.commit()
    return {"message":"yeet!"}