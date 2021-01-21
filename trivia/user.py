from flask import render_template,redirect,url_for,session,g,Blueprint,request,flash
import functools

from auth import login_required

from db import get_db

bp = Blueprint('user',__name__)




@bp.route('/index')
@login_required
def index():
    contador = 0
    if session.get('user_id') is None:
        return redirect(url_for('auth.inicio'))
    else:
        db,c = get_db()
        c.execute(
            'select username from usuario where id = %s',(session.get('user_id'),)
        )
        user = c.fetchone()
        c.execute(
            'select * from partida where user_id = %s',(session.get('user_id'),)
        )
        match = c.fetchall()
        for match in match:
            if match['completed'] == 1:
                contador+=1
    return render_template('user/index.html',user=user,match=match,contador=contador)



