from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector
import json

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root1234'
app.config['MYSQL_DB'] = 'python'

app.secret_key = 'secret_key'

mysql = mysql.connector.connect(
    host=app.config['MYSQL_HOST'],
    user=app.config['MYSQL_USER'],
    password=app.config['MYSQL_PASSWORD'],
    database=app.config['MYSQL_DB']
)


class Phone():
    def __init__(self, id, brand, model, price):
        self.id = id
        self.brand = brand
        self.model = model
        self.price = price

    def __repr__(self):
        return f'<Phone {self.id}>'

    def __json__(self):
        return {'id': self.id, 'brand': self.brand, 'model': self.model, 'price': self.price}


class User():
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User {self.username}>'


@app.route('/')
def toLogin():
    return redirect(url_for('login'))


@app.route('/index')
def index():
    cur = mysql.cursor()
    cur.execute("SELECT * FROM phones")
    phones = []
    for id, brand, model, price in cur.fetchall():
        phones.append(Phone(id=id, brand=brand, model=model, price=price))
    cur.close()
    return render_template('index.html', phones=phones)


@app.route('/echarts')
def echarts():
    cur = mysql.cursor()
    cur.execute("SELECT * FROM phones")
    phones = []
    for id, brand, model, price in cur.fetchall():
        phones.append(Phone(id=id, brand=brand, model=model, price=price))
    cur.close()
    phones = json.dumps([phone.__json__() for phone in phones])
    return render_template('echarts.html', phones=phones)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        brand = request.form['brand']
        model = request.form['model']
        price = request.form['price']
        cur = mysql.cursor()
        cur.execute("INSERT INTO phones (brand, model, price) VALUES (%s,%s, %s)", (brand, model, price))
        mysql.commit()
        cur.close()
        return redirect(url_for('index'))
    return render_template('add.html')


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    cur = mysql.cursor()
    cur.execute("SELECT * FROM phones WHERE id = %s", (id,))
    phone = cur.fetchone()
    if request.method == 'POST':
        brand = request.form['brand']
        model = request.form['model']
        price = request.form['price']
        cur.execute("UPDATE phones SET brand = %s, model = %s, price = %s WHERE id = %s", (brand, model, price, id))
        mysql.commit()
        cur.close()
        return redirect(url_for('index'))
    cur.close()
    return render_template('edit.html', phone=phone)


@app.route('/delete/<int:id>')
def delete(id):
    cur = mysql.cursor()
    cur.execute("DELETE FROM phones WHERE id = %s", (id,))
    mysql.commit()
    cur.close()
    return redirect(url_for('index'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cur = mysql.cursor()
        cur.execute("SELECT * FROM users WHERE username = %s", (username,))
        user = cur.fetchone()
        if user is None:
            error = 'Invalid Credentials. Please try again.'
            return render_template('login.html', error=error)
        else:
            if user:
                session['username'] = user[1]
                return redirect(url_for('index'))
            else:
                error = 'Invalid Credentials. Please try again.'
                return render_template('login.html', error=error)
        cur.close()
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cur = mysql.cursor()
        cur.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        mysql.commit()
        cur.close()
        return redirect(url_for('login'))
    return render_template('register.html')


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
