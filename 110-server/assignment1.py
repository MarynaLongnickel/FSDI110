from flask import Flask, jsonify

app = Flask(__name__)

# Root welcome page
@app.route("/", methods=["GET"])
def welcome():
    return "<h1>Welcome to My REST API</h1><p>Use the /about page to learn more.</p>"

# About page
@app.route("/about", methods=["GET"])
def about():
    return "<h2>About This API</h2><p>This is a simple product catalog API built with Flask.</p>"

# Sample product catalog
products = [
    {"id": 1, "name": "Cake", "price": 25},
    {"id": 2, "name": "Icecream", "price": 5},
    {"id": 3, "name": "Cookie", "price": 3},
    {"id": 4, "name": "Chocolate", "price": 10}
]

# Get all products
@app.route("/api/product", methods=["GET"])
def get_products():
    return jsonify(products)

# Get count of products
@app.route("/api/product/count", methods=["GET"])
def get_product_count():
    return jsonify({"count": len(products)})

if __name__ == "__main__":
    app.run(debug=True)