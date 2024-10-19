from flask import Flask, request, jsonify

app = Flask(__name__)

# Login route
@app.route('/login', methods=['POST'])
def login():
    # Get the JSON data from the request
    data = request.json
    email = data.get('email')
    password = data.get('password')
    
    # Dummy login logic (replace with your actual database logic)
    if email == "student@example.com" and password == "password123":
        return jsonify({"message": "Login successful", "token": "fake-jwt-token"}), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401

if __name__ == '__main__':
    app.run(debug=True)
