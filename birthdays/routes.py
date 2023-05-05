from flask import render_template, url_for, flash, redirect, request
from birthdays import app, db, bcrypt
from birthdays.forms import RegistrationForm, LoginForm, NewEntry
from birthdays.models import User, Data
from flask_login import login_user, current_user, logout_user, login_required


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/index", methods=['GET', 'POST'])
@login_required
def index():
    form = NewEntry()
    if request.method == 'POST':
        if db.session.query(Data).filter(Data.name == form.name.data).count() != 0:
            flash('Birthday already exists!', 'danger')
        else:
            entry = Data(name=form.name.data, day=form.day.data,
                        month=form.month.data, author=current_user)
            db.session.add(entry)
            db.session.commit()
            flash(f'Birthday added for {form.name.data}!', 'success')
    birthdays = Data.query.filter_by(author=current_user)
    return render_template('index.html', birthdays=birthdays, form=NewEntry())

@app.route('/delete/<int:birthday_id>', methods=['POST'])
def delete_birthday(birthday_id):
    birthday = Data.query.get_or_404(birthday_id)
    db.session.delete(birthday)
    db.session.commit()
    flash('Birthday deleted successfully', 'success')
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if (form.validate_on_submit()):
        hashed_password = bcrypt.generate_password_hash(
            form.password.data).decode('utf-8')
        user = User(username=form.username.data, email= form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(
            f'Account created for {form.username.data}! You can log in now', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            flash('Logged in!', 'success')
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('index'))
        else:
            flash('Login unsuccessful. Please check email and password!', 'danger')
    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))
