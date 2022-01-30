from flask import Blueprint
from controllers.controller import RestaurantController

'''
Restaurant blueprint for the API endpoints
CRUD operations for restaurants

get_restaurants: get all restaurants
get_restaurant: get a restaurant by name
get_a_random_restaurant: get a random restaurant
add_restaurant: add a restaurant
delete_restaurant: delete a restaurant by name
update_restaurant: update a restaurant by name
'''
restaurantRoutes = Blueprint('restaurantRoutes', __name__)
restaurantRoutes.route('', methods=['GET'])(RestaurantController.get_restaurants)
restaurantRoutes.route('/<string:name>', methods=['GET'])(RestaurantController.get_restaurant)
restaurantRoutes.route('/random', methods=['GET'])(RestaurantController.get_a_random_restaurant)
restaurantRoutes.route('', methods=['POST'])(RestaurantController.add_restaurant)
restaurantRoutes.route('<string:name>', methods=['DELETE'])(RestaurantController.delete_restaurant)
restaurantRoutes.route('/<string:name>', methods=['PUT'])(RestaurantController.update_restaurant)