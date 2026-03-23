from flask import Flask

def create_app():
    """
    The Application Factory. 
    This is where the 'AgeOverflow' system will eventually start.
    """
    app = Flask(__name__)

    # We import the 'api' Blueprint from our routes file
    from .views.routes import api
    
    # This registers all our URLs under the /api/v1 prefix
    app.register_blueprint(api)

    return app
