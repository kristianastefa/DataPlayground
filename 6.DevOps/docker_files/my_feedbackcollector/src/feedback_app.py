from flask import Flask, request, jsonify
from prometheus_client import Gauge, generate_latest
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.DEBUG)

RMSE_GAUGE = Gauge('feedbackcollector_rmse', 'Root Mean Squared Error')
USER_COUNT = Gauge('feedbackcollector_user_count', 'Number of unique users')

feedback_data = {
    'errors': [],
    'unique_users': set(),
    'squared_errors': [],
}

@app.route('/feedback', methods=['GET'])
def feedback():
    try:
        user_id = int(request.args.get('userid'))
        item_id = int(request.args.get('itemid'))
        actual_score = float(request.args.get('rating'))
        estimated_score = float(request.args.get('estimated_rating'))
        print(user_id,item_id,actual_score,estimated_score, flush =True)
        # Calculate squared error
        error = actual_score - estimated_score
        squared_error = error ** 2

        # Update metrics
        feedback_data['unique_users'].add(user_id)
        feedback_data['squared_errors'].append(squared_error)

        print(f"Updated squared errors: {feedback_data['squared_errors']}", flush=True)
        print(f"Unique users: {feedback_data['unique_users']}",flush=True)

        if len(feedback_data['squared_errors']) > 0:
            rmse = (sum(feedback_data['squared_errors']) / len(feedback_data['squared_errors'])) ** 0.5
        else:
            rmse = 0.0

        unique_users = len(feedback_data['unique_users'])
        RMSE_GAUGE.set(rmse)
        USER_COUNT.set(unique_users)

        print(f"Calculated RMSE: {rmse}", flush=True)
        print(f"Number of unique users: {unique_users}", flush=True)
        print(f"Calculated Gauge RMSE: {RMSE_GAUGE}", flush=True)
        print(f"Number of GAUGE unique users: {USER_COUNT}", flush=True)

        response = {
            'rmse': rmse,
            'unique_users': unique_users
        }
        return jsonify(response), 200

    except Exception as e:
        print(f"Error processing feedback: {e}", flush=True)
        response = {
            'error': str(e)
        }
        return jsonify(response), 500

@app.route('/metrics')
def metrics():
    return generate_latest(), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
