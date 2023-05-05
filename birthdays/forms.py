from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, BooleanField, EmailField, PasswordField, ValidationError
from wtforms.validators import DataRequired, Length, number_range, Email, EqualTo
from birthdays.models import User


class NewEntry(FlaskForm):
    name = StringField(name='name', validators=[
                       DataRequired(), Length(min=2, max=20)], render_kw={"placeholder": "Name"})
    day = IntegerField(name='day', validators=[
                       DataRequired(), number_range(min=1, max=31)], render_kw={"placeholder": "Day"})
    month = IntegerField(name='month', validators=[
                         DataRequired(), number_range(min=1, max=12)], render_kw={"placeholder": "Month"})
    delete = BooleanField(name='delete')
    submit = SubmitField('Add Birthday')


class RegistrationForm(FlaskForm):
    username = StringField(name='username', validators=[
        DataRequired(), Length(min=2, max=20)])
    email = EmailField(name='Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField(
        'Confirm Password', validators=[DataRequired(), EqualTo('password')])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Signup')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('This username is already taken!')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('This email is already taken!')


class LoginForm(FlaskForm):
    email = EmailField(name='email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
    remember = BooleanField('Remember Me')