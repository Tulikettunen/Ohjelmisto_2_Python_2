from flask import Flask

app = Flask(__name__)
@app.route('/mikämikäohjelma/<teksti1>/<teksti2>')
def kaiku(teksti1, teksti2):
    vastaus = {
        "Haiku" : teksti1 + " " + teksti2 + " muodostavat haiun"
    }
    return vastaus

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)