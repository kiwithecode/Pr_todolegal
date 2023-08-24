from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
from datetime import datetime

app = Flask(__name__)
CORS(app)

WEBHOOK_URL = "https://webhook.site/60ec9d8e-fd7f-4b68-82aa-ab23ce5ffde2"
ALLOWED_EXTENSIONS = set(['pdf', 'doc', 'docx', 'txt'])

# Check for allowed file types
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
@app.route('/send_data', methods=['POST'])
def send_data():
    # Extract name from the incoming request
    name = request.form.get('name', '')  # If no name is provided, use an empty string

    local_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    ip_address = request.remote_addr

    # Check if file was sent
    if 'file' not in request.files:
        return jsonify(status="error", message="No file provided")
    
    file = request.files['file']

    if file.filename == '':
        return jsonify(status="error", message="No file selected")

    if file and allowed_file(file.filename):
        files = {'file': (file.filename, file.stream)}
        data = {
            'name': name,
            'local_time': local_time,
            'ip_address': ip_address
        }
        response = requests.post(WEBHOOK_URL, data=data, files=files)

        return jsonify(status=response.status_code, text=response.text)
    else:
        return jsonify(status="error", message="File type not allowed")


if __name__ == '__main__':
    app.run(debug=True)
