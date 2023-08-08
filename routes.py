from flask import render_template
from app import app

@app.route('/')
def index():
    return render_template('inicio.html')

@app.route('/biografia')
def biografia():
    biografia = {'nombre': 'Carlos Corona', 'edad': 25, 'hobbies': ['programar', 'jugar videojuegos', 'leer']}
    return render_template('biografia.html', biografia=biografia)

@app.route('/proyectos')
def proyectos():
    return render_template('proyectos.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')
