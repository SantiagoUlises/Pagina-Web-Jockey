from flask import Flask, render_template, url_for
import os
app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/Directivos')
def directivos():
    return render_template('Directivos.html')

@app.route('/Contacto')
def contacto():
    return render_template('Contacto.html')

@app.route('/Galerias')
def galerias():
    imagen_archivo = os.path.join(app.root_path, 'static/galeria')
    images = [f'galeria/{image}' for image in os.listdir(imagen_archivo) if image.endswith(('jpg','jpeg','png','gif'))]
    return render_template('Galerias.html', images=images)

@app.route('/Agenda')
def agenda():
    return render_template('Agenda.html')

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
