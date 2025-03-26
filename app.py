import boto3
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# Initialize AWS Bedrock client
bedrock_client = boto3.client(
    'bedrock-runtime',
    region_name='us-east-1'  # Change to your AWS region
)

# Function to generate response using Bedrock
def generate_response(user_input):
    payload = {
        "prompt": user_input,
        "max_tokens": 200
    }
    
    try:
        response = bedrock_client.invoke_model(
            body=json.dumps(payload),
            modelId="anthropic.claude-v2"
        )
        response_body = json.loads(response['body'].read().decode('utf-8'))
        return response_body.get("completion", "Error: No response")
    except Exception as e:
        return f"Error: {str(e)}"

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        if not data or "query" not in data:
            return jsonify({"error": "Query cannot be empty"}), 400
        
        user_query = data["query"].strip()
        if not user_query:
            return jsonify({"error": "Query cannot be empty"}), 400
        
        ai_response = generate_response(user_query)
        return jsonify({"response": ai_response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
