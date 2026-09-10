from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/converter_temperartura', methods=['POST'])
def converter_temperartura():
    celsius = float(request.form['celcius'])

    fahrenheit = (celsius * 9 / 5) + 32

    return render_template('index.html', fahrenheit=fahrenheit)

if __name__ == '__main__':
    app.run(debug=True)