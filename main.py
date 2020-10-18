from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

mysql = MySQL(app)

app.secret_key = 'mysecret'
# Connec Database
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'ome0895114530'
app.config['MYSQL_DB'] = 'pythonlogin'

url="https://www.goldtraders.or.th/AvgPriceList.aspx"

def january():
    web_data = requests.get(url)
    soup = BeautifulSoup(web_data.text,'html.parser')
    find_word = soup.find_all("table",{"id":"DetailPlace_MainGridView"},"tbody")
    for i in find_word:
        i=str(i).split('มกราคม')[1]
        i=str(i).split('</font>')[1]
        i=str(i).split('<td align="right"><font color="Black" face="Tahoma,Verdana" size="1">')[1]
        i=str(i).split(',')
        i=i[0]+i[1]
        return float(i)
def febuary():
    web_data = requests.get(url)
    soup = BeautifulSoup(web_data.text,'html.parser')
    find_word = soup.find_all("table",{"id":"DetailPlace_MainGridView"},"tbody")
    for i in find_word:
        i=str(i).split('กุมภาพันธ์')[1]
        i=str(i).split('</font>')[1]
        i=str(i).split('<td align="right"><font color="Black" face="Tahoma,Verdana" size="1">')[1]
        i=str(i).split(',')
        i=i[0]+i[1]
        return float(i)
def march():
    web_data = requests.get(url)
    soup = BeautifulSoup(web_data.text,'html.parser')
    find_word = soup.find_all("table",{"id":"DetailPlace_MainGridView"},"tbody")
    for i in find_word:
        i=str(i).split('มีนาคม')[1]
        i=str(i).split('</font>')[1]
        i=str(i).split('<td align="right"><font color="Black" face="Tahoma,Verdana" size="1">')[1]
        i=str(i).split(',')
        i=i[0]+i[1]
        return float(i)
def april():
    web_data = requests.get(url)
    soup = BeautifulSoup(web_data.text,'html.parser')
    find_word = soup.find_all("table",{"id":"DetailPlace_MainGridView"},"tbody")
    for i in find_word:
        i=str(i).split('เมษายน')[1]
        i=str(i).split('</font>')[1]
        i=str(i).split('<td align="right"><font color="Black" face="Tahoma,Verdana" size="1">')[1]
        i=str(i).split(',')
        i=i[0]+i[1]
        return float(i)
def may():
    web_data = requests.get(url)
    soup = BeautifulSoup(web_data.text,'html.parser')
    find_word = soup.find_all("table",{"id":"DetailPlace_MainGridView"},"tbody")
    for i in find_word:
        i=str(i).split('พฤษภาคม')[1]
        i=str(i).split('</font>')[1]
        i=str(i).split('<td align="right"><font color="Black" face="Tahoma,Verdana" size="1">')[1]
        i=str(i).split(',')
        i=i[0]+i[1]
        return float(i)
def june():
    web_data = requests.get(url)
    soup = BeautifulSoup(web_data.text,'html.parser')
    find_word = soup.find_all("table",{"id":"DetailPlace_MainGridView"},"tbody")
    for i in find_word:
        i=str(i).split('มิถุนายน')[1]
        i=str(i).split('</font>')[1]
        i=str(i).split('<td align="right"><font color="Black" face="Tahoma,Verdana" size="1">')[1]
        i=str(i).split(',')
        i=i[0]+i[1]
        return float(i)
def july():
    web_data = requests.get(url)
    soup = BeautifulSoup(web_data.text,'html.parser')
    find_word = soup.find_all("table",{"id":"DetailPlace_MainGridView"},"tbody")
    for i in find_word:
        i=str(i).split('กรกฎาคม')[1]
        i=str(i).split('</font>')[1]
        i=str(i).split('<td align="right"><font color="Black" face="Tahoma,Verdana" size="1">')[1]
        i=str(i).split(',')
        i=i[0]+i[1]
        return float(i)
def august():
    web_data = requests.get(url)
    soup = BeautifulSoup(web_data.text,'html.parser')
    find_word = soup.find_all("table",{"id":"DetailPlace_MainGridView"},"tbody")
    for i in find_word:
        i=str(i).split('สิงหาคม')[1]
        i=str(i).split('</font>')[1]
        i=str(i).split('<td align="right"><font color="Black" face="Tahoma,Verdana" size="1">')[1]
        i=str(i).split(',')
        i=i[0]+i[1]
        return float(i)
def september():
    web_data = requests.get(url)
    soup = BeautifulSoup(web_data.text,'html.parser')
    find_word = soup.find_all("table",{"id":"DetailPlace_MainGridView"},"tbody")
    for i in find_word:
        i=str(i).split('กันยายน')[1]
        i=str(i).split('</font>')[1]
        i=str(i).split('<td align="right"><font color="Black" face="Tahoma,Verdana" size="1">')[1]
        i=str(i).split(',')
        i=i[0]+i[1]
        return float(i)
def october():
    web_data = requests.get(url)
    soup = BeautifulSoup(web_data.text,'html.parser')
    find_word = soup.find_all("table",{"id":"DetailPlace_MainGridView"},"tbody")
    for i in find_word:
        i=str(i).split('ตุลาคม')[1]
        i=str(i).split('</font>')[1]
        i=str(i).split('<td align="right"><font color="Black" face="Tahoma,Verdana" size="1">')[1]
        i=str(i).split(',')
        i=i[0]+i[1]
        return float(i)

month=[]

month.append(january())
month.append(febuary())
month.append(march())
month.append(april())
month.append(may())
month.append(june())
month.append(july())
month.append(august())
month.append(september())
month.append(october())
#month.append
#month.append

cal=(month[0]+month[1]+month[2]+month[3]+month[4]+month[5]+month[6]+month[7]+month[8]+month[9])/len(month)
fortune = cal - month[-1]
print(cal)
print (fortune)

plt.figure(figsize=(12,6))
left = [1, 2, 3, 4, 5,6,7,8,9,10] 
  
height = month
  
tick_label = ['january','febuary','march','april','may','june','july','august','september','october'] 

plt.bar(left, height, tick_label = tick_label,
        width = 0.2,align='edge', color = ['red', 'green']) 
  

plt.title('Gold chart!') 

plt.savefig('static\images\my_plot1.png')


















@app.route('/', methods=['GET', 'POST'])
def login():
    # Output message if something goes wrong
    msg = ''
    # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        # Check if account exists using MySQL
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = %s AND password = %s', (username, password,))
        # Fetch one record and return result
        account = cursor.fetchone()
        # If account exists in accounts table in out database
        if account:
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            # Redirect to home page
            return redirect(url_for('home'))
        else:
            # Account doesnt exist or username/password incorrect
            msg = 'Incorrect username/password!'
    # Show the login form with message (if any)
    return render_template('index.html', msg=msg)

# http://localhost:5000/python/logout - this will be the logout page
@app.route('/pythonlogin/logout')
def logout():
    # Remove session data, this will log the user out
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    # Redirect to login page
    return redirect(url_for('login'))

@app.route('/pythonlogin/register', methods=['GET', 'POST'])
def register():
    # Output message if something goes wrong...
    msg = ''
    # Check if "username", "password" and "email" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
                # Check if account exists using MySQL
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = %s', (username,))
        account = cursor.fetchone()
        # If account exists show error and validation checks
        if account:
            msg = 'Account already exists!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address!'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers!'
        elif not username or not password or not email:
            msg = 'Please fill out the form!'
        else:
            # Account doesnt exists and the form data is valid, now insert new account into accounts table
            cursor.execute('INSERT INTO accounts VALUES (NULL, %s, %s, %s)', (username, password, email,))
            mysql.connection.commit()
            msg = 'You have successfully registered!'
    elif request.method == 'POST':
        # Form is empty... (no POST data)
        msg = 'Please fill out the form!'
    # Show registration form with message (if any)
    return render_template('register.html', msg=msg)


@app.route('/pythonlogin/home')
def home():
    # Check if user is loggedin
    if 'loggedin' in session:
        
        return render_template('home.html', username=session['username'],prophecy=fortune,calcu=cal,oct=month[-1],sep=month[-2],aug=month[-3],jul=month[-4],jun=month[-5],may=month[-6],apr=month[-7],mar=month[-8],feb=month[-9],jan=month[-10])
    # User is not loggedin redirect to login page
    return redirect(url_for('login'))

@app.route('/pythonlogin/profile')
def profile():
    # Check if user is loggedin
    if 'loggedin' in session:
        # We need all the account info for the user so we can display it on the profile page
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE id = %s', (session['id'],))
        account = cursor.fetchone()
        # Show the profile page with account info
        return render_template('profile.html', account=account)
    # User is not loggedin redirect to login page
    return redirect(url_for('login'))


    
if __name__ == '__main__' :
    app.run(debug=True)
