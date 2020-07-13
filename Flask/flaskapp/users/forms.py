import re
from wtforms.validators import (ValidationError, DataRequired, EqualTo, 
                                Length, Email)
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from flask_wtf import FlaskForm
from flaskapp.models import User
from flask_wtf.file import FileField, FileAllowed 
from flask_login import current_user

def password_validate(form, field):
        if len(field.data) < 8:
            raise ValidationError("Make sure your password is at lest 8 characters.")
        elif re.search('\d', field.data) is None:
            raise ValidationError("Make sure your password contains a number.")
        elif re.search('[A-Z]', field.data) is None:
            raise ValidationError("Make sure your password contains an upper case letter.")
        elif re.search('[a-z]', field.data) is None:
            raise ValidationError("Make sure your password contains a lower case letter.")
        elif re.search('[!£$_=+\'?><,.{}\[\]%|`¬^&*@~#\"]', field.data) is None:
            raise ValidationError("Make sure your password contains a special character.")


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators= [DataRequired(), Length(min= 5, max= 20)])
    email = StringField('Email',
                        validators= [DataRequired(), Email(check_deliverability= True)])
    password = PasswordField('Password', 
                             validators= [DataRequired(), password_validate])
    password_confirmation = PasswordField('Confirm Password', 
                             validators= [DataRequired(), EqualTo('password', message= 'This does not match your previous password.')])
    submit = SubmitField('Register')
    
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')
    
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')

class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators= [DataRequired(), Email(check_deliverability= True)])
    password = PasswordField('Password', 
                             validators= [DataRequired()])
    remember = BooleanField('Remember Me')
    
    submit = SubmitField('Log in')
    
    
class UpdateAccountForm(FlaskForm):
    username = StringField('Username',
                           validators= [DataRequired(), Length(min= 5, max= 20)])
    email = StringField('Email',
                        validators= [DataRequired(), Email(check_deliverability= True)])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')
    
    
    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken. Please choose a different one.')
    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose a different one.')
                
class RequestResetForm(FlaskForm):
    email = StringField('Email', 
                        validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')
    
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('There is no account with that email. You must register first.')
            
class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', 
                             validators= [DataRequired(), password_validate])
    password_confirmation = PasswordField('Confirm Password', 
                             validators= [DataRequired(), EqualTo('password', message= 'This does not match your previous password.')])
    submit = SubmitField('Reset Password')