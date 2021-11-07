from endpoints.books_api import app

books_app = app

if __name__ == "__main__":
    books_app.run(debug=True)