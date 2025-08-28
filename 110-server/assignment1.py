from flask import Flask, jsonify, request

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
    {"id": 1, "name": "Cake", "price": 25, "category": "Dessert"},
    {"id": 2, "name": "Icecream", "price": 5, "category": "Dessert"},
    {"id": 3, "name": "Cookie", "price": 3, "category": "Snack"},
    {"id": 4, "name": "Chocolate", "price": 10, "category": "Snack"},
    {"id": 5, "name": "Pizza", "price": 15, "category": "Main"}
]

# In-memory coupon storage
coupons = [
    {'name': 'save10', 'discount': 0.10},
    {'name': 'save50', 'discount': 0.50}
]


# ---------- Product Endpoints ----------

# Get all products
@app.route("/api/product", methods=["GET"])
def get_products():
    return jsonify(products)

# Get count of products
@app.route("/api/product/count", methods=["GET"])
def get_product_count():
    return jsonify({"count": len(products)})

# Get products by category
@app.route("/api/product/category/<string:category>", methods=["GET"])
def get_products_by_category(category):
    filtered = [p for p in products if p["category"].lower() == category.lower()]
    return jsonify(filtered)

# Get products by max price (<= given price)
@app.route("/api/product/price/<int:max_price>", methods=["GET"])
def get_products_by_price(max_price):
    filtered = [p for p in products if p["price"] <= max_price]
    return jsonify(filtered)

# Search product by title
@app.route("/api/product/search", methods=["GET"])
def search_product_by_name():
    query = request.args.get("q", "")
    filtered = [p for p in products if query.lower() in p["name"].lower()]
    return jsonify(filtered)


# ---------- Coupon Endpoints ----------

# Save coupon
@app.route("/api/coupon", methods=["POST"])
def save_coupon():
    data = request.json
    if not data or "name" not in data or "discount" not in data:
        return jsonify({"error": "Invalid coupon format"}), 400
    coupons.append(data)
    return jsonify({"message": "Coupon saved", "coupon": data}), 201

# Retrieve all coupons
@app.route("/api/coupon", methods=["GET"])
def get_coupons():
    return jsonify(coupons)

# Search coupon by name
@app.route("/api/coupon/<coupon_name>", methods=["GET"])
def search_coupon_by_name(coupon_name):
    filtered = [c for c in coupons if coupon_name.lower() in c["name"].lower()]
    return jsonify(filtered)


# Run the app
if __name__ == "__main__":
    app.run(debug=True)
