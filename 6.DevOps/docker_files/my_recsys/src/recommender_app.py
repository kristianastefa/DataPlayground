from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# Load the trained SVD model
with open('../models/model_SVD.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/recommend', methods=['GET'])
def recommend():
    user_id = request.args.get('userid')
    item_id = request.args.get('itemid')

    if user_id is None or item_id is None:
        return jsonify({'error': 'Missing parameters'}), 400

    try:
        user_id = int((user_id))  
        item_id = int((item_id))  
        estimated_rating = model.predict(user_id, item_id).est
        return jsonify({'estimated_rating': estimated_rating})
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
if __name__ == '__main__':
    app.run(host='0.0.0.0')
