from flask import Flask,render_template, url_for,redirect
app = Flask(__name__)
@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/Directivos')
def directivos():
    return render_template(url_for('Directivos.html'))

@app.route('/Contacto')
def contacto():
    return render_template(url_for('Contacto.html'))

@app.route('/Galerias')
def galerias():
    return render_template(url_for('Galerias.html'))

@app.route('/Agenda')
def agenda():
    return render_template(url_for('Agenda.html'))

@app.route('/login')
def login():
    return render_template(url_for('login.html'))

if __name__=='__main__':
    app.run(debug=True)