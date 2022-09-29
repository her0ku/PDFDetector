import os
from flask import Flask, render_template, request, flash, redirect, url_for, session
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'Mystery key Exodus'
UPLOAD_FOLDER = '/uploads/pdf/'
ALLOWED_EXTENSIONS = {'png', 'jpeg', 'pdf', 'doc'}


def allowed_files(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
@app.route('/mainPage', methods=['GET', 'POST'])
async def call_main_page():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_files(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('download_file', name=filename))
    if request.method == 'GET':
        return render_template('home.html')


@app.errorhandler(404)
def handle_404(e):
    # handle all other routes here
    return render_template('flag.html')


if __name__ == '__main__':
    app.run()
