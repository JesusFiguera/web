from flask import render_template,redirect,url_for,session,g,Blueprint,request,flash


import functools

from werkzeug.security import generate_password_hash,check_password_hash

from db import get_db


bp = Blueprint('auth',__name__)





@bp.route('/')
def inicio():
    return render_template('inicio.html')



@bp.route('/register',methods=['POST','GET'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db,c = get_db()
        c.execute(
            'select username from usuario where username = %s',(username,)
        )
        user = c.fetchone()
        if not user:
            c.execute(
                'insert into usuario (username,password) values (%s,%s)',(username,generate_password_hash(password))
            )
            db.commit()
            return redirect(url_for('auth.login'))
        if user is not None:
            flash('Usuario existente, intenta denuevo.')
    elif session.get('user_id') is not None:
        return redirect(url_for('auth.index'))
    return render_template('auth/register.html')


@bp.route('/login',methods=['POST','GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db,c = get_db()
        c.execute(
            'select id,username,password from usuario where username = %s',(username,)
        )
        user = c.fetchone()
        if not user:
            flash('Datos invalidos.')
        elif user['username'] == username and check_password_hash(user['password'],password):
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('user.index'))
        elif not check_password_hash(user['password'],password):
            flash('Datos invalidos')
    return render_template('auth/login.html')


@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.inicio'))


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if session.get('user_id') is None:
            return redirect(url_for('auth.inicio'))

        return view(**kwargs)
    return wrapped_view











