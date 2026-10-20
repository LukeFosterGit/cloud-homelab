import os

import psycopg
from flask import Flask

app = Flask(__name__)

def get_db_connection():
	return psycopg.connect(
		host=os.environ["DB_HOST"],
		dbname=os.environ["DB_NAME"],
		user=os.environ["DB_USER"],
		password=os.environ["DB_PASSWORD"],
	)


@app.route("/")
def home():
	return """
	<h1>Cloud Homelab Application</h1>
	<p>Flask is running inside Docker.</p>
	<p>Try <a href="/messages">/messages</a></p>
	"""

@app.route("/health")
def health():
	return {"status":"healthy"}, 200

@app.route("/messages")
def messages():
	with get_db_connection() as connection:
		with connection.cursor() as cursor:
			cursor.execute("SELECT id, message FROM messages ORDER BY id;")
			rows = cursor.fetchall()

	output = "<h1>Messages</h1>"

	for row in rows:
		output += f"<p>{row[0]}: {row[1]}</p>"

	return output

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000)
