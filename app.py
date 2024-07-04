from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector
import os
app = Flask(__name__)
app.secret_key = 'secret'
def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='uliseskapo98@',
        database='common',
    )

@app.route('/')
def inicio():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM noticias ORDER BY fecha DESC')
    noticias = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', noticias=noticias)

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


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        conn=get_db_connection()
        cursor=conn.cursor()
        cursor.execute('SELECT * FROM usuarios WHERE email = %s AND password = %s', (email, password))
        user=cursor.fetchone()
        cursor.close()

        if user:
            session['user_id'] = user[0]
            return redirect(url_for('inicio'))
        else:
            return 'Email o contraseña incorrectos'
    return render_template('login.html')

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO usuarios (email,password) VALUES (%s, %s)',(email, password)) 
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('login'))
    return render_template('registro.html')

@app.route('/subir', methods=['GET', 'POST'])
def subir():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        titulo = request.form['titulo']
        contenido = request.form['contenido']
        imagen = request.files['imagen']

        imagen_filename = None
        if imagen:
            imagen_filename = os.path.join('static/uploads', imagen.filename)
            imagen.save(imagen_filename)
        
        conn= get_db_connection()
        cursor=conn.cursor()
        cursor.execute('INSERT INTO noticias (titulo , contenido , imagen) VALUES (%s, %s, %s)',(titulo,contenido,imagen_filename))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('inicio'))
    return render_template('subir.html')

if __name__ == '__main__':
    app.run(debug=True)
