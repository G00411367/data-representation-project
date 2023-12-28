# This Flask application performs CRUD operations on MySql database



from flask import Flask, url_for,request, redirect, abort, jsonify, session
from productDAO import coffeeDAO as dao
app = Flask(__name__, static_url_path = "", static_folder = "staticpages")


# Root to home page
@app.route("/")
def index():
    return app.send_static_file("home.html")

# Gets all data from the database
@app.route('/home')
def getAll():
    return jsonify(dao.getAll())

# Get data specified by id
@app.route("/home/<id>")
def findByID(id):
    return jsonify(dao.findById(id))


# Add new reccord to the database
@app.route('/home', methods=['POST'])
def createCoffee():
    if not request.json:
        abort(400)
    data = {
        "CoffeeName":request.json["CoffeeName"],
        "Origin":request.json["Origin"],
        "Variety":request.json["Variety"],
        "Roast":request.json["Roast"],
        "Price":request.json["Price"],
        
    }
    print("Created entry", data)
    return jsonify(dao.create(data))


# Update database from the webpage
@app.route('/home/<id>', methods = ['PUT'])
def update(id):
    foundCoffee = dao.findById(id)
    print("Updated entry", foundCoffee)
    if len(foundCoffee) == 0:
        return jsonify ({}), 404
    currentCoffee = foundCoffee
    if "CoffeeName" in request.json:
        currentCoffee["CoffeeName"] = request.json["CoffeeName"]
    if "Origin" in request.json:
        currentCoffee["Origin"] = request.json["Origin"]
    if "Variety" in request.json:
        currentCoffee["Variety"] = request.json["Variety"]
    if "Roast" in request.json:
        currentCoffee["Roast"] = request.json["Roast"]
    if "Price" in request.json:
        currentCoffee["Price"] = request.json["Price"]
   
    dao.update(currentCoffee)
    return jsonify(currentCoffee)


# Delete by id
@app.route('/home/<id>', methods = ['DELETE'])
def delete(id):
    foundCoffee = dao.findById(id)
    print("Deleted entry", foundCoffee)
    if len(foundCoffee) == 0:
        return jsonify ({}), 404
    dao.delete(id)
    return jsonify({"done":True})



if __name__ == "__main__":
    app.run(debug=True, port=8080)
