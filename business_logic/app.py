from flask import Flask, render_template, request, redirect, url_for, jsonify
import os 
app = Flask(__name__, template_folder="templates")

@app.route('/', methods = ['GET'])
def index():
    return render_template('index.html')

@app.route('/services', methods=['GET','POST'])
def handle_button_click():
    data = request.json
    button_clicked = data.get('buttonClicked')
    # Perform actions based on the button clicked
    if button_clicked == 'roadCrack':
        # Redirect or perform actions for road crack detection
        return redirect(os.getenv("ROAD_CRACK_DETECTION_URL"))
    elif button_clicked == 'buildingCrack':
        # Redirect or perform actions for building crack detection
        return redirect(os.getenv("MERGED_CRACK_DETECTION_URL"))
    elif button_clicked == 'trafficSign':
        # Redirect or perform actions for traffic sign detection
        return redirect(os.getenv("ROAD_TRAFFIC_SIGN_DETECTION_URL"))
    else:
        return jsonify(error='Invalid button click event')

if __name__ == "__main__":
    app.run(debug=True,host = "0.0.0.0", port = os.getenv("PORT"))
