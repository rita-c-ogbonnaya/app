from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=["GET"])
def get_info():
    response = {
        "email": "rytha7273@gmail.com",  
        "current_datetime": datetime.utcnow().isoformat() + "Z",
        "github_url": "https://github.com/rita-c-ogbonnaya/app.git"   
    }
    return jsonify(response), 200

if __name__ == "__main__":
    app.run(debug=True)
