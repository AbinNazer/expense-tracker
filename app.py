from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Persistent storage (temporary for now)
total = 0

@app.route("/", methods=["GET", "POST"])
def index():
    global total
    if request.method == "POST":
        amount = float(request.form.get("amount", 0))
        action = request.form.get("action")
        if action == "add":
            total += amount
        elif action == "subtract":
            total -= amount
        return redirect(url_for("index"))
    return render_template("index.html", total=total)

if __name__ == "__main__":
    app.run(debug=True)
