from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello_world():
    return "<p>Hello World!</p>"

@app.route("/FSDI110")
def hi():
    return "<h1>Hello Cohort #59</h1>"

@app.get('/home')
def home():
    print("Home endpoint accessed.")
    return "Welcome to the home page!"

@app.get('/api/students')
def students():
    print('Students endpoint accessed')
    student_names = ['Britney', 'Alex', 'James', 'David']
    return student_names

# Path parameter
@app.get("/greet/<string:name>")
def greet(name):
    return f"Hello {name}"

@app.get('/contact')
def contact_api():
    print('Contact API endpoint accessed')
    user = {'name': 'peter', 'age': 35}
    return user

students = [
    {'id': 1, 'name': 'Bruce', 'age': 54, 'email': 'batman@gmail.com'},
    {'id': 2, 'name': 'Pam', 'age': 29, 'email': 'pam@gmail.com'}
]

@app.get('/students')
def get_students():
    return students

@app.post('/students')
def post_students():
    data = request.json
    students.append(data)
    return students

app.run(debug=True)