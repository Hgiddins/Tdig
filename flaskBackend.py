from flask import Flask, jsonify
import Federal_Treasuries
import Repo_Rates
import time


app = Flask(__name__)

@app.route('/api/refresh_all', methods=['POST'])
def refresh_all():
    start_time = time.time()  # Record the start time

    try:
        Federal_Treasuries.update_federal_treasuries()
        Repo_Rates.update_historic_repo_rates()
        end_time = time.time()  # Record the end time
        execution_time = end_time - start_time  # Calculate the total execution time
        print(f"Execution time: {execution_time:.2f} seconds")  # Print the execution time to 2 decimal places
        return jsonify(success=True, message="Sheet updated successfully!"), 200
    except Exception as e:
        return jsonify(success=False, message=str(e)), 500


if __name__ == '__main__':
    # app.run(host='0.0.0.0', debug=True)
    app.run(debug=True)
