from website import create_app, create_database
from database import *
from os import path

app = create_app()

if __name__ == '__main__':
    create_database(app)
    app.run(debug=True)