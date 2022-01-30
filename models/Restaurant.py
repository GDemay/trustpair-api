from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify, request
from database.config import db

class Restaurant(db.Model):
  '''
  Restaurant model

  id (int): unique id for the restaurant
  name (string): name of the restaurant
  description (string): description of the restaurant
  '''
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80), unique=True, nullable=False)
  description = db.Column(db.String(250))
  
  def serialize(self):
      return {
          'id': self.id,
          'name': self.name,
          'description': self.description,
      }
      
  def __reppr__(self):
    return f"{self.name} - {self.description}"