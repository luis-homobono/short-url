from crypt import methods
from flask import Flask, render_template, flash, url_for, request, redirect, jsonify
from flask_mysql_connector import MySQL
import mysqlx
import shortuuid

app = Flask(__name__)

# endpoint = "http://short.url"
endpoint = "http://localhost"

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "****"
app.config["MYSQL_PASSWORD"] = "*****"
app.config["MYSQL_DATABASE"] = "db_enlaces_cortos"

mysql = MySQL(app)

@app.route("/", methods=["GET"])
def index():
    try:
        return jsonify(respuesta="Inicio")
    except:
        return jsonify(respuesta="Error en petición"), 500

@app.route("/create_url_short", methods=["POST"])
def create_url_short():
    try:
        if request.method == "POST":
            url = request.form["url"]
            cursor = mysql.connection.cursor()

            short_url = shortuuid.ShortUUID().random(length=7)

            cursor.execute("INSERT INTO enlaces (url, enlace_corto) VALUES (%s, %s)", (url, short_url))

            mysql.connection.commit()
            cursor.close()

            new_url = endpoint + "/" + short_url
            return jsonify(respuesta=new_url)
    except:
        return jsonify(respuesta="Error en petición"), 500

if __name__ == "__main__":
    app.run(port=80, debug=True)