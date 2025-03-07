from flask import Flask, request, render_template, redirect, url_for, abort, flash, session
import sqlite3

app = Flask(__name__)
app.secret_key = "supersecretkey"

images = {
    "waffle": {"title": "Waffle", "filename": "image-waffle-desktop.jpg", "price":"6.50"},
    "creme-brulee": {"title": "Creme-Brulee", "filename": "image-creme-brulee-desktop.jpg", "price":"7.00"}, 
    "macaron": {"title": "Macaron", "filename": "image-macaron-desktop.jpg", "price":"8.00"},
    "tiramisu": {"title": "Tiramisu", "filename": "image-tiramisu-desktop.jpg", "price":"5.50"},
    "baklava": {"title": "Baklava", "filename": "image-baklava-desktop.jpg", "price":"4.00"}, 
    "meringue": {"title": "Meringue", "filename": "image-meringue-desktop.jpg", "price":"5.00"}, 
    "cake": {"title": "Vanilla Cake", "filename": "image-cake-desktop.jpg", "price":"9.00"},
    "brownie": {"title": "Brownie", "filename": "image-brownie-desktop.jpg", "price":"4.50"},
    "panna-cotta": {"title": "Panna-Cotta", "filename": "image-panna-cotta-desktop.jpg", "price":"6.50"},
}

@app.route('/')
def home():
    return render_template ("home.html", images=images)

@app.route('/details/<image_id>') 
def details(image_id):
    image = images.get(image_id)
    if not image:
        return "Image not found", 404
    return render_template("details.html", image=image)


if __name__ == '__main__':
    app.run(debug=True)