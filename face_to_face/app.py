from flask import Flask, render_template


app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    colours = ['Beck', 'Alemão', 'Maciel']
    return render_template('index.html', colours=colours)

if __name__ == "__main__":
    app.run(debug=True)

# https://stackoverflow.com/questions/45877080/how-to-create-dropdown-menu-from-python-list-using-flask-and-html
