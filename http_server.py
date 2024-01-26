from flask import Flask, request, jsonify
import os

app = Flask(__name__)

DATA_DIR = 'C:/Users/Suhas/OneDrive/Desktop/assignment'


@app.route('/data', methods=['GET'])
def get_data():
    # Get query parameters
    file_name = request.args.get('n')
    line_number = request.args.get('m')

    # Check if 'n' parameter is provided
    if file_name is None:
        return jsonify({"error": "'n' parameter is required"}), 400

    file_path = os.path.join(DATA_DIR, 'randomfile.txt')

    # Check if the file exists
    if not os.path.exists(file_path):
        return jsonify({"error": "File ''randomfile.txt'' not found"}), 404

    # Check if 'm' parameter is provided
    if line_number is not None:
        try:
            line_number = int(line_number)
            with open(file_path, 'r') as file:
                lines = file.readlines()
                if 1 <= line_number <= len(lines):
                    return jsonify({"content": lines[line_number - 1].strip()})
                else:
                    return jsonify({"error": f"Invalid line number: {line_number}"}), 400
        except ValueError:
            return jsonify({"error": "'m' parameter must be an integer"}), 400

    # If only 'n' is provided, return the entire content of the file
    with open(file_path, 'r') as file:
        content = file.read()
        return jsonify({"content": content.strip()})

if __name__ == '__main__':
    app.run(debug=True)
