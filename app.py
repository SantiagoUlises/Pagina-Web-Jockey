from flask import Flask, render_template, request, redirect, url_for, session
import pymysql
import os

import pymysql.cursors
app = Flask(__name__)
app.secret_key = 'secret'
app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'static/uploads')
def get_db_connection():
    conn=pymysql.connect(host='localhost',   
                                user='root',
                                password='uliseskapo98@',
                                database='common',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)
    return conn

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
        url = request.form.get('url', '')

        imagen = request.files['imagen']

        imagen_filename = None
        if imagen:
            imagen_filename = imagen.filename
            imagen_filename = imagen_filename.replace("/", "\\")  # Convertir barras diagonales a barras invertidas
            imagen.save(os.path.join(app.config['UPLOAD_FOLDER'], imagen_filename))
        
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO noticias (titulo, contenido, imagen, url) VALUES (%s, %s, %s, %s)', (titulo, contenido, imagen_filename, url))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('inicio'))

    # Obtener las noticias de la base de datos y pasarlas a la plantilla
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT id, titulo, contenido, imagen, url FROM noticias')
    news_items = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('subir.html', news_items=news_items)



@app.route('/eliminar/<int:id>', methods=['POST'])
def eliminar_noticia(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM noticias WHERE id = %s', (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('subir'))  # Redirigir a la página de subir después de eliminar

if __name__ == '__main__':
    app.run(debug=True)
