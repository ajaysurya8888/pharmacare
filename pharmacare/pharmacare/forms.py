from flask_wtf import FlaskForm
from wtforms import StringField, DateField ,IntegerField ,PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo
class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')
    print = SubmitField('print')

class addItemForm(FlaskForm):
    itemName=StringField('item name',validators=[DataRequired()])
    pkdDate=DateField('packed Date', format='%d/%m/%Y')
    expDate=DateField('expiry Date', format='%d/%m/%Y')
    quantity=IntegerField('quantity',validators=[DataRequired()])
    price=IntegerField('price',validators=[DataRequired()])
    add = SubmitField('add')
class billItemForm(FlaskForm):
    itemName=StringField('item name', validators=[DataRequired()])
    quantity=IntegerField('quantity',validators=[DataRequired()])
    price = IntegerField('price',validators=[DataRequired()])
    enter=SubmitField('enter')
    clear=SubmitField('clear')
