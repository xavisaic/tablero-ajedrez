from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def tablero8x8 (num=4, num2=4):
    return render_template('index.html', num=num, num2=num2)

@app.route('/4')
def tablero8x4 (num=2, num2=4):
    return render_template('index.html', num=num, num2=num2)


@app.route('/<int:num>/<int:num2>')
def tableroxy (num, num2):
    return render_template('index.html', num=num, num2=num2)







if __name__ == '__main__':
    app.run(debug=True)