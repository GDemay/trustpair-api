import requests

URL = "http://0.0.0.0:5000/"

def test_IsServerOn():
  '''
  This test is for checking if the server is running.
  '''
  response = requests.get(URL)
  assert response.status_code == 200

def test_getRestaurantThatDoesNotExists():
  '''
    This test is for checking a restaurant that does not exists in database. 
    Return code should be 404.
  '''
  response = requests.get(URL + "restaurants/ThisRestaurantDoesNotExists")
  assert response.status_code == 404

def test_getAllRestaurant():
  '''
    This test is for getting all restaurants.
    return code should be 200.
  '''
  response = requests.get(URL + "restaurants")
  assert response.status_code == 200

def test_AddRestaurant():
  '''
    This test is for adding a restaurant.
    return code should be 200.
  '''
  response = requests.post(URL + "restaurants", json={"name": "TestRestaurant", "description": "Test description"})
  assert response.status_code == 200
  
def test_CreateSameRestaurant():
  '''
    This test is for creating a restaurant that already exists.
    return code should be 403.
  '''
  response = requests.post(URL + "restaurants", json={"name": "TestRestaurant", "description": "Test description"})
  assert response.status_code == 403

def test_getRandomRestaurant():
  '''
    This test is for get a random restaurant.
    return code should be 200.
  '''
  response = requests.get(URL + "restaurants/random")
  assert response.status_code == 404

def test_getRandomRestaurant():
  ''' 
    This test is for get a second time a random restaurant.
    return code should be 200.
  '''
  response = requests.get(URL + "restaurants/TestRestaurant")
  assert response.status_code == 200

def test_getTestRestaurant():
  '''
    This test is for getting a restaurant that exists
    return code should be 200.
  '''
  response = requests.get(URL + "restaurants/TestRestaurant")
  assert response.status_code == 200

def test_updateTestRestaurant():
  '''
    This test is for updating a restaurant that exists.
    return code should be 200.
  '''
  response = requests.put(URL + "restaurants/TestRestaurant", json={"name": "NewTestRestaurant", "description": "Other description"})
  assert response.status_code == 200
      
def test_updateRestaurantsThatDoesNotExists():
  '''
    This test is for updating a restaurant that does not exist.
    return code should be 409.
  '''
  response = requests.put(URL + "restaurants/BlablaTestDuResto", json={"name": "Trustpair restaurant", "description": "Pizza, Burger, French fries"})
  assert response.status_code == 409
  
def test_deleteTestRestaurant():
  '''
    This test is for deleting a restaurant.
    return code should be 200.
  '''
  response = requests.delete(URL + "restaurants/NewTestRestaurant")
  assert response.status_code == 200