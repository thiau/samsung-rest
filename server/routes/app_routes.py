from server import app, jsonify


@app.route('/app/status')
def app_status():
	return jsonify(status="Running")