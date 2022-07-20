from crypt import methods
from flask import Flask, render_template, flash, url_for, request, redirect, jsonify
from flask_mysql_connector import MySQL
from config import DevConfig
import shortuuid

app = Flask(__name__)
app.config.from_object(DevConfig)

# endpoint = "http://short.url"
endpoint = "http://localhost"

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

            while True:
                short_url = shortuuid.ShortUUID().random(length=7)
                cursor.execute("SELECT * FROM enlaces WHERE enlace_corto = BINARY %s", (short_url))

                if not cursor.fetchone():
                    break

            cursor.execute("SELECT enlace_corto FROM enlaces WHERE url = BINARY %s", (url,))

            data = cursor.fetchone()
            if data:
                new_url = endpoint + "/" + data[0]
                return jsonify(respuesta=new_url), 200

            cursor.execute("INSERT INTO enlaces (url, enlace_corto) VALUES (%s, %s)", (url, short_url))

            mysql.connection.commit()
            cursor.close()

            new_url = endpoint + "/" + short_url
            return jsonify(respuesta=new_url), 200
    except Exception as e:
        return jsonify(respuesta=f"Error en petición {e}"), 500

@app.route("/<id>")
def get_url(id):
    try:
        cursor = mysql.connection.cursor()

        cursor.execute("SELECT url FROM enlaces WHERE enlace_corto = BINARY %s", (id,))
        data = cursor.fetchone()

        cursor.close()

        return jsonify(respuesta=data[0]), 200
    except:
        return jsonify(respuesta=f"Error en petición {e}"), 500

if __name__ == "__main__":
    app.run(port=80, debug=True)