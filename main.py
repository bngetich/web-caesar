from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>

<head>
    <style>
        form {{
            background-color: #eee ;
            padding: 20px;
            margin: 0 auto;
            width: 540px;
            font: 16px sans-serif;
            border-radius: 10px;
        }}
        textarea {{
            margin: 25px 0px 10px 0px;
            width: 540px;
            height: 120px; 
        }}
    </style>
</head>

<body>
    <form method="POST">
        <label for="rotateBy">
            <b>Rotate by:<b>
        </label>
        <input id="rotateBy" type="text" name="rot" value="0">
        <textarea name="text">{0}</textarea>
        <button type="submit">Submit Query</button>
    </form>
</body>

</html>
"""


@app.route("/")
def index():
    return form.format("")


@app.route("/", methods=['POST'])
def encrypt():
    rot = request.form['rot']
    text = request.form['text']
    rotated_string = rotate_string(text, int(rot))

    return form.format(rotated_string)


app.run()
