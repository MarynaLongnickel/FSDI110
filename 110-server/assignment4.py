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

# ---------- Product Data ----------
products_list = [
    {"id": 1, "title": "Laptop", "category": "Electronics", "price": 899.99},
    {"id": 2, "title": "Headphones", "category": "Electronics", "price": 199.99},
    {"id": 3, "title": "Coffee Mug", "category": "Kitchen", "price": 12.50},
    {"id": 4, "title": "Notebook", "category": "Stationery", "price": 5.99}
]


# ---------- Product Endpoints ----------

# Get all products
@app.route("/products", methods=["GET"])
def get_products():
    return jsonify(products_list)

# Get products by category
@app.route("/products/category/<string:category>", methods=["GET"])
def get_products_by_category(category):
    filtered = [p for p in products_list if p["category"].lower() == category.lower()]
    return jsonify(filtered)

# Get products by max price
@app.route("/products/price/<float:max_price>", methods=["GET"])
def get_products_by_price(max_price):
    filtered = [p for p in products_list if p["price"] <= max_price]
    return jsonify(filtered)

# Search product by title (substring match)
@app.route("/products/search/<string:title>", methods=["GET"])
def search_product_by_title(title):
    filtered = [p for p in products_list if title.lower() in p["title"].lower()]
    return jsonify(filtered)


# Run the app
if __name__ == "__main__":
    app.run(debug=True)
