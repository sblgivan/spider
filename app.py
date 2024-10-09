from flask import Flask, request, jsonify
from flask_ngrok import run_with_ngrok
import os

# Initialize the Flask app
app = Flask(__name__)
run_with_ngrok(app)  # Start ngrok when the app is run

@app.route('/')
def index():
    return send_from_directory(os.getcwd(), 'index.html')

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    query = data.get('query', '')

    # Here you can implement your AI logic
    response = f"You asked: {query}. (This is a mock response)"
    
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run()
  
