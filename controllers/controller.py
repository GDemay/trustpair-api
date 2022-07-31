from flask import request, jsonify, request
from models.Restaurant import Restaurant
from flask import jsonify, request
from database.config import db

class RestaurantController:
  def get_restaurants():
    """[Get all restaurants from the database]

    Returns:
        [JSON] -- [List of restaurants]
    """
    restaurants = Restaurant.query.all()
    return jsonify([r.serialize() for r in restaurants])

  def get_restaurant(self):
    """[Get a restaurant from name in the database]

    Args:
        name ([string]): name of the restaurant

    Returns:
        [JSON]: [Return the restaurant object]
    """
    restaurant = Restaurant.query.filter_by(self=self).first()
    if restaurant is None:
      return jsonify({"message": "Restaurant not found"}), 404
    return restaurant.serialize()

  def get_a_random_restaurant():
    """[Get a random restaurant from the database]

    Returns:
        [JSON]: [Return the restaurant object]
    """
    restaurant = Restaurant.query.order_by(db.func.random()).first()
    if restaurant is None:
      return jsonify({"message": "Restaurant not found"}), 404
    return restaurant.serialize()

  def add_restaurant():
    """[Add a restaurant to the database]

    Returns:
        [JSON]: [Return the restaurant object]
    """
    restaurant = Restaurant(name=request.json['name'], description=request.json['description'])  
    if Restaurant.query.filter_by(name=restaurant.name).first() is not None:
      return jsonify({"message": "Restaurant already exists"}), 403
    if restaurant is None:
      return jsonify({"message": "Restaurant not found"}), 404
    db.session.add(restaurant)
    db.session.commit()
    return restaurant.serialize()

  def delete_restaurant(self):
    """[Delete a restaurant from the database]

    Args:
        name ([string]): [The name of the restaurant to delete]

    Returns:
        [JSON]: [Message of success or failure]
    """
    restaurant = Restaurant.query.filter_by(self=self).first()
    if restaurant is None:
      return jsonify({"message": "Conflict error with Restaurant object"}), 409
    db.session.delete(restaurant)
    db.session.commit()
    return {'message': 'Restaurant deleted'}

  def update_restaurant(self):
    """[Update a restaurant from the database]

    Args:
        name ([string]): [The name of the restaurant to update]

    Returns:
        [JSON]: [Return the restaurant object]
    """
    restaurant = Restaurant.query.filter_by(self=self).first()
    if restaurant is None:
      return jsonify({"message": "Conflict error with Restaurant object"}), 409
    restaurant.name = request.json['name']
    restaurant.description = request.json['description']
    db.session.commit()
    return restaurant.serialize()  