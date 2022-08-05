from extensions import (
    Blueprint,
    app,
    os,
    render_template
)   

api = Blueprint('user', 'user')

@api.route('/')
def home():
    return render_template('test.html')