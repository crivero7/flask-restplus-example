# run.py

import os

# local imports
from app import create_app

app = create_app("development")

if __name__ == "__main__":

    app.run()
    # app.run(host='0.0.0.0', port=8080)