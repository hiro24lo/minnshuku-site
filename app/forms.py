from flask_wtf import FlaskForm
from wtforms import StringField, DateField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email
from flask_sqlalchemy import SQLAlchemy
from wtforms import PasswordField
from wtforms.validators import Length



class ReservationForm(FlaskForm):
    name = StringField('お名前', validators=[DataRequired()])
    email = StringField('メールアドレス', validators=[DataRequired(), Email()])
    checkin = DateField('チェックイン日', validators=[DataRequired()])
    checkout = DateField('チェックアウト日', validators=[DataRequired()])
    message = TextAreaField('ご要望')
    submit = SubmitField('予約する')

class AdminLoginForm(FlaskForm):
    password = PasswordField('管理者パスワード', validators=[DataRequired(), Length(min=4)])
    submit = SubmitField('ログイン')
