from flask import Flask, request, abort, jsonify
from flask_cors import CORS
from models.models import setup_db, db
from app_util import App_Util

def create_app(test_config=None):

    app = Flask(__name__)
    setup_db(app)
    CORS(app)
    App_Util.register_blueprints(app)

    '''
        The after_request decorator to set Access-Control-Allow
    '''
    @app.after_request
    def after_request(response):
        response.headers.add(
            'Access-Control-Allow-Methods',
            'GET,POST,PATCH,DELETE,OPTIONS'
        )
        return response

    @app.route('/')
    def home():
        return 'Hello!'

    @app.errorhandler(400)
    def bad_request(error):
        return handle_error(400, 'Bad request')

    @app.errorhandler(404)
    def not_found(error):
        return handle_error(404, 'Not found')

    @app.errorhandler(422)
    def unprocessable_entity(error):
        return handle_error(422, 'Unprocessable entity')

    def handle_error(code, message):
        return jsonify({
            'success': False,
            'error': code,
            'message': message
        }), code

    return app


app = create_app()

if __name__ == '__main__':
    app.run(debug=True, )
