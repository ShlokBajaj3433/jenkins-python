import os

from flask import Flask, jsonify, render_template

app = Flask(__name__)


@app.get("/")
def home():
	return render_template("base.html", title="Northstar Commerce | Python Home", content=render_template("home.html"))


@app.get("/catalog")
def catalog():
	return render_template("base.html", title="Northstar Commerce | Catalog", content=render_template("catalog.html"))


@app.get("/cart")
def cart():
	return render_template("base.html", title="Northstar Commerce | Cart", content=render_template("cart.html"))


@app.get("/checkout")
def checkout():
	return render_template("base.html", title="Northstar Commerce | Checkout", content=render_template("checkout.html"))


@app.get("/enterprise")
def enterprise():
	return render_template("base.html", title="Northstar Commerce | Enterprise", content=render_template("enterprise.html"))


@app.get("/health")
def health():
	return jsonify({"status": "ok", "project": "python"})


if __name__ == "__main__":
	port = int(os.getenv("PORT", "5000"))
	app.run(host="0.0.0.0", port=port)
