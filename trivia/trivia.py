from flask import render_template,redirect,url_for,session,g,Blueprint,request,flash
import functools
import time

from auth import login_required

from db import get_db

bp = Blueprint('trivia',__name__,url_prefix='/trivia')

@bp.route('/categorias')
@login_required
def categorias():
    return render_template('trivia/categorias.html')


@bp.route('/categoria1',methods=['POST','GET'])
@login_required
def categoria1():
    completed = False
    contador = 0
    respuestas = []
    from preguntas import preguntas1,respuestas1
    pregunta = preguntas1
    respuesta = respuestas1
    if request.method == 'POST':
        respuestas = [
            request.form[str(1)],
            request.form[str(2)],
            request.form[str(3)],
            request.form[str(4)],
            request.form[str(5)],
            request.form[str(6)],
            request.form[str(7)],
            request.form[str(8)],
            request.form[str(9)],
            request.form[str(10)]
        ]
        for respuesta1 in respuestas:
            if respuesta1 == 'True':
                contador+=1
        if contador == 10:
            completed = True
        db,c = get_db()
        c.execute(
            'insert into partida (user_id,num_correctas,completed,categoria) values (%s,%s,%s,%s)',(session.get('user_id'),contador,completed,'Entretenimiento')
        )
        db.commit()
        return redirect(url_for('user.index'))
    return render_template('trivia/categoria1.html',pregunta=pregunta,respuesta=respuesta,rango=len(pregunta))

@bp.route('/categoria2',methods=['POST','GET'])
@login_required
def categoria2():
    completed = False
    contador = 0
    respuestas = []
    from preguntas import preguntas2,respuestas2
    pregunta = preguntas2
    respuesta = respuestas2
    if request.method == 'POST':
        respuestas = [
            request.form[str(1)],
            request.form[str(2)],
            request.form[str(3)],
            request.form[str(4)],
            request.form[str(5)],
            request.form[str(6)],
            request.form[str(7)],
            request.form[str(8)],
            request.form[str(9)],
            request.form[str(10)]
        ]
        for respuesta1 in respuestas:
            if respuesta1 == 'True':
                contador+=1
        if contador == 10:
            completed = True
        db,c = get_db()
        c.execute(
            'insert into partida (user_id,num_correctas,completed,categoria) values (%s,%s,%s,%s)',(session.get('user_id'),contador,completed,'Comida')
        )
        db.commit()
        return redirect(url_for('user.index'))
    return render_template('trivia/categoria2.html',pregunta=pregunta,respuesta=respuesta,rango=len(pregunta))