from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def root():
    return "flask application version 1.3"

# Ensure no non-printable characters in the following line
app.run(host="0.0.0.0", port=4000)

