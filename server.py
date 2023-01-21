import csv
import os

from flask import Flask, render_template, send_from_directory, request, redirect

app = Flask(__name__)


@app.route("/")
def home_page():
    return render_template("index.html")


@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f"\n{email}, {subject}, {message}")


def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_to_file(data)
            write_to_csv(data)
            return redirect('thankyou.html')
        except:
            return "did not save to database"
    else:
        return "Something went wrong."
