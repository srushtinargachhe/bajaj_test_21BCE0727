from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/bfhl', methods=['POST', 'GET'])
def bfhl():
    if request.method == 'POST':
        data = request.json.get('data', [])
        numbers = [item for item in data if item.isdigit()]
        alphabets = [item for item in data if item.isalpha()]
        highest_lowercase_alphabet = [max([ch for ch in alphabets if ch.islower()], default='')]
        
        response = {
            "is_success": True,
            "user_id": "john_doe_17091999",  # Replace with actual logic or variables
            "email": "john@xyz.com",  # Replace with actual logic or variables
            "roll_number": "ABCD123",  # Replace with actual logic or variables
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_lowercase_alphabet": highest_lowercase_alphabet
        }
        
        return jsonify(response)

    elif request.method == 'GET':
        response = {
            "operation_code": 1
        }
        return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)
