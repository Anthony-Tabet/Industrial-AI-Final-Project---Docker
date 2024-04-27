# from flask import Flask, render_template, request, redirect, url_for, jsonify
# import os 
# app = Flask(__name__, template_folder="templates")

# @app.route('/', methods = ['GET'])
# def index():
#     return render_template('index.html')

# @app.route('/services', methods=['GET', 'POST'])
# def handle_button_click():
#     content_type = request.headers.get('Content-Type')
#     if content_type is None or content_type != 'application/json':
#         return jsonify(error='Unsupported Media Type'), 415

#     data = request.json
#     if data is None or 'buttonClicked' not in data:
#         return jsonify(error='Invalid JSON data'), 400

#     button_clicked = data['buttonClicked']
#     # Perform actions based on the button clicked
#     if button_clicked == 'roadCrack':
#         # Redirect or perform actions for road crack detection
#         return redirect(os.getenv("ROAD_CRACK_DETECTION_URL"))
#     elif button_clicked == 'buildingCrack':
#         # Redirect or perform actions for building crack detection
#         return redirect(os.getenv("MERGED_CRACK_DETECTION_URL"))
#     elif button_clicked == 'trafficSign':
#         # Redirect or perform actions for traffic sign detection
#         return redirect(os.getenv("ROAD_TRAFFIC_SIGN_DETECTION_URL"))
#     else:
#         return jsonify(error='Invalid button click event'), 400

from flask import Flask, render_template, redirect, url_for
from flask_cors import CORS
import os

app = Flask(__name__, template_folder="templates")
CORS(app)

@app.route('/services', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/road_crack_detection')
def road_crack_detection():
    print(os.getenv("ROAD_CRACK_DETECTION_URL"))  # Print the value of ROAD_CRACK_DETECTION_URL
    return redirect(os.getenv("ROAD_CRACK_DETECTION_URL"))

@app.route('/road_sign_detection')
def road_sign_detection():
    print(os.getenv("ROAD_TRAFFIC_SIGN_DETECTION_URL"))  # Print the value of ROAD_TRAFFIC_SIGN_DETECTION_URL
    return redirect(os.getenv("ROAD_TRAFFIC_SIGN_DETECTION_URL"))

@app.route('/building_crack_detection')
def building_crack_detection():
    print(os.getenv("MERGED_CRACK_DETECTION_URL"))  # Print the value of MERGED_CRACK_DETECTION_URL
    return redirect(os.getenv("MERGED_CRACK_DETECTION_URL"))

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=os.getenv("PORT"))

