from flask import Flask
from api.routes.auth import auth_blueprint
from api.routes.data import data_blueprint

app = Flask(__name__)
app.register_blueprint(auth_blueprint, url_prefix='/auth')
app.register_blueprint(data_blueprint, url_prefix='/data')

@app.route('/')
def home():
    return 'API is running!'

if __name__ == '__main__':
    app.run(debug=True)

