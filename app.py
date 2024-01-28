from flask import Flask, render_template, request
import blockchain

app = Flask(__name__)

# Tu mogą być funkcje obsługujące logikę gry

@app.route('/')
def index():
    return render_template('index.html')  # Strona główna kasyna

@app.route('/play', methods=['GET', 'POST'])
def play():
    if request.method == 'POST':
        # Logika gry
        pass
    return render_template('play.html')  # Strona z grą

@app.route('/transaction', methods=['POST'])
def transaction():
    # Logika transakcji kryptowalutowej
    pass

if __name__ == '__main__':
    app.run(debug=True)
