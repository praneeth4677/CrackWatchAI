from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
import os

from predict import predict_model

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')

@app.route('/predict/', methods=['POST'])
def predict():
    if request.method == 'POST':
        f = request.files['file']
        print("in post")
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'static\\images', secure_filename(f.filename))
        print("filepath:",file_path)
        f.save(file_path)
        print("after save")
        label,confidence=predict_model(file_path)
        print("before result")
        return render_template('pred.html',pred=label,confidence=confidence,f_name=f.filename)

    return None


if __name__ == '__main__':
    app.run(debug=True)

