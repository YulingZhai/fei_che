#
#
# def init_route(app):
#
#     @app.route('/')
#     def hello_world():
#         return 'hello World'

from .index import blue

def init_view(app):
    app.register_blueprint(blue)
