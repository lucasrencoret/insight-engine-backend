import json
from flask import Flask, jsonify, abort, make_response, request, url_for

app = Flask(__name__)


# @auth.login_required
@app.route('/<string:query>', methods=['GET'])
def get_tasks(query):
    with open('query_specs.json') as fd:
        json_data = json.load(fd)
    # json_data[query]
    if query not in json_data:
        abort(404)

    return jsonify({query: json_data[query]})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(debug=True)
