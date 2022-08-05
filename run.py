import imp
from app.controller.service_controller import api
from extensions import app
# register the api
app.register_blueprint(api)


if __name__ == '__main__':
    app.run('localhost', 8080, debug=True)

