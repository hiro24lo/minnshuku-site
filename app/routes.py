from flask import Blueprint, render_template
from app.forms import ReservationForm 
from flask_sqlalchemy import SQLAlchemy
from app.models import Reservation
from app import db
from app.forms import AdminLoginForm
from flask import redirect, url_for, session, flash



# ブループリントの設定
main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/rooms')
def rooms():
    return render_template('rooms.html')

@main.route('/plans')
def plans():
    return render_template('plans.html')

@main.route('/reservation', methods=['GET', 'POST'])  # ← POST 追加
def reservation():
    form = ReservationForm()
    if form.validate_on_submit():
        # フォーム送信時の処理（あとでここに保存・メール送信などを書く）
        reservation = Reservation(
            name = form.name.data,
            email = form.email.data,
            checkin = form.checkin.data,
            checkout = form.checkout.data,
            message = form.message.data
        )
        db.session.add(reservation)
        db.session.commit()
        return render_template('thank_you.html', name=form.name.data)

    return render_template('reservation.html', form=form)  # ← formを渡す


@main.route('/contact')
def contact():
    return render_template('contact.html')


ADMIN_PASSWORD = 'admin123'  # 簡易パスワード（本番では.envで管理！）

@main.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    form = AdminLoginForm()
    if form.validate_on_submit():
        if form.password.data == ADMIN_PASSWORD:
            session['admin_logged_in'] = True
            return redirect(url_for('main.reservation_list'))
        else:
            flash('パスワードが間違っています')
    return render_template('admin_login.html', form=form)

@main.route('/reservations')
def reservation_list():
    if not session.get('admin_logged_in'):
        return redirect(url_for('main.admin_login'))

    reservations = Reservation.query.order_by(Reservation.created_at.desc()).all()
    return render_template('reservations.html', reservations=reservations)
