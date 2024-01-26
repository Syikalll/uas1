from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Syikal Cesi Felicia Sawotong (2119113938), Sistem Informasi"

if __name__ == "__main__":
    app.run(host='0.0.0.0')

