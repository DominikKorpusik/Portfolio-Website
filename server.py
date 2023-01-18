import os
from flask import Flask, render_template, send_from_directory, url_for

app = Flask(__name__)

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')
