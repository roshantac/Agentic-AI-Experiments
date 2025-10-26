from flask import Flask, request, jsonify
from flask_cors import CORS
import perception
import memory
import decision
app = Flask(__name__)
CORS(app)  # Allow frontend access

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")
    print(f"Genie received: {user_message}")  # Log the query
    resp = perception.handle(user_message)
    print(f"Perception respnse :{resp}")    
    resp = memory.query_internal_memory(resp)
    print(f"Memory respnse :{resp}")
    resp = decision.tool_caller(resp)
    return jsonify({"response": resp})

if __name__ == "__main__":
    app.run(debug=True)
