from flask import render_template, request, jsonify
from app import app
from app.recommendation import get_refined_options

@app.route('/')
def index():
    food_types = [
        'American', 'Italian', 'Mexican', 'Asian', 'Seafood', 
        'Fast Food', 'Sandwiches & Deli', 'Pizza', 'Steak & BBQ', 
        'Other International', 'Other'
    ]
    return render_template('index.html', food_types=food_types)

@app.route('/get_refined_options', methods=['POST'])
def get_refined_options_route():
    selected_food_type = request.json['selected_food_type']
    options = get_refined_options(selected_food_type)
    return jsonify(options)
