from flask import Flask, render_template, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/simulate', methods=['POST'])
def simulate():
    # Get data from the frontend
    data = request.json

    # Call the Python script with the provided data
    subprocess.run(['python', 'simulation_script.py', data['param1'], data['param2']])

    # Return the path to the generated image
    image_path = 'path/to/generated/image.png'
    return jsonify({'image_path': image_path})

if __name__ == '__main__':
    app.run(debug=True)
