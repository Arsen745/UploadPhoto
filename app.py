from flask import Flask, render_template, request, jsonify, redirect, url_for
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return jsonify(success=False)
        file = request.files['file']
        if file.filename == '':
            return jsonify(success=False)
        if file:
            filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return jsonify(success=True)

    images = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('upload.html', images=images)


if __name__ == '__main__':
    app.run(debug=True)
