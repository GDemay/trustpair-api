from routes.restaurantRoutes import restaurantRoutes
from database.config import app

app.register_blueprint(restaurantRoutes, url_prefix='/restaurants')

# This endpoint is for testing purposes only.
@app.route('/')
def index():
  return {'message': 'Hello World!'}

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')