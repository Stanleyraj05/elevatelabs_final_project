from flask import Flask, request

# Initialize Flask app
app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    # Handle incoming POST request
    data = request.json
    # Your logic to process the data goes here
    return "Webhook received!", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

