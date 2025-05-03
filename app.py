from flask import Flask, request, jsonify

app = Flask(__name__)

@app.before_request
def log_request_info():
    print(f"🔍 {request.method} {request.path} from {request.remote_addr}")

@app.route('/Account/AppLogin', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    print(f"🔥 Login attempt → Username: {username}, Password: {password}")

    return jsonify({
        "UserName": username or "Unknown",
        "ExpiredDate": "2035-01-01",
        "Money": 999999
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
