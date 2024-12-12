# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


ads = [
    {"id": 1, "title": "ноутбук msi", "description": "отличное состояние и производительность", "price": 20000},
    {"id": 2, "title": "аккаунт VALORANT", "description": "123ммр,15скинов", "price": 15000},
]

@app.route('/')
def index():
    return render_template('index.html', ads=ads)

@app.route('/add_ad', methods=['GET', 'POST'])
def add_ad():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        price = request.form['price']
        new_ad = {"id": len(ads) + 1, "title": title, "description": description, "price": price}
        ads.append(new_ad)
        return redirect(url_for('index'))
    return render_template('add_ad.html')

if __name__ == '__main__':
    app.run(debug=True)