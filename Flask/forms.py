from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
import re

def password_validate(form, field):
        if len(field.data) < 8:
            raise ValidationError("Make sure your password is at lest 8 characters. ")
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
    

class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators= [DataRequired(), Email(check_deliverability= True)])
    password = PasswordField('Password', 
                             validators= [DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Log in')
    
  
    
    
