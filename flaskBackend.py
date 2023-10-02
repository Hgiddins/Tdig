from flask import Flask, jsonify
import Sheets_API

app = Flask(__name__)

@app.route('/api/refresh_all', methods=['POST'])
def refresh_all():
    try:
        Sheets_API.update_sheet()
        return jsonify(success=True, message="Sheet updated successfully!"), 200
    except Exception as e:
        return jsonify(success=False, message=str(e)), 500

if __name__ == '__main__':
    app.run(debug=True)
