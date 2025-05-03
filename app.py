from flask import Flask, request, jsonify

app = Flask(__name__)

# Ghi log mọi request đến
@app.before_request
def log_request_info():
    print(f"🔍 {request.method} {request.path} from {request.remote_addr}")

# Xử lý đăng nhập từ phần mềm
@app.route('/Account/AppLogin', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    print(f"🔥 Login attempt → Username: {username}, Password: {password}")

    if username == 'admin' and password == '123456':
        return jsonify({
            "UserName": "MrTTS",
            "ExpiredDate": "2035-01-01",
            "Money": 999999
        })
    else:
        return jsonify({
            "UserName": "Unknown",
            "ExpiredDate": "2025-01-01",
            "Money": 0
        })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
