from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import data_required, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from flaskapp.models import User


class RegistrationFrom(FlaskForm):
    username = StringField('Username', validators=[data_required(), Length(min=5, max=15)])
    email = StringField('Email', validators=[data_required(), Email()])
    password = PasswordField('Password', validators=[data_required()])
    confrim_password = PasswordField('Confrim Password', validators=[data_required(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError(' This username is already exist')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError(' This email-id is already exist')

class LoginFrom(FlaskForm):
    email = StringField('Email', validators=[data_required(), Email()])
    password = PasswordField('Password', validators=[data_required()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class UpdateAccountFrom(FlaskForm):
    username = StringField('Username', validators=[data_required(), Length(min=5, max=15)])
    email = StringField('Email', validators=[data_required(), Email()])
    picture =FileField('Update Profile', validators=[FileAllowed(['jpg', 'jpeg', 'png'])])
    submit = SubmitField('Update Account')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError(' This username is already exist')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError(' This email-id is already exist')

class RequestResetForm(FlaskForm):
    email = StringField('Email', validators=[data_required(), Email()])
    submit = SubmitField('Request Reset Password')   

    def validate_email(self, email):
            user = User.query.filter_by(email=email.data).first()
            if user is None:
                raise ValidationError(' There is no account registered with this e-mail')

class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[data_required()])
    confrim_password = PasswordField('Confrim Password',
     validators=[data_required(), EqualTo('password')])
    submit = SubmitField('Reset Password')
