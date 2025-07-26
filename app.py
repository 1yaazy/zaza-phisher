from flask import Flask, render_template, request

app = Flask(__name__, template_folder="subdir/templates", static_folder="static")

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")
        print(f"Username: {username}, Password: {password}")
        # You can also log or process them as needed here
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)