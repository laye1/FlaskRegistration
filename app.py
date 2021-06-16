from flask import Flask,render_template,request,redirect,url_for,flash,session
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3




app = Flask(__name__)

app.config['SECRET_KEY'] = 'cryptographies'

def get_connection():
    conn = sqlite3.connect('mabase.db')
    conn.row_factory = sqlite3.Row
    


    return conn

@app.route('/')

def index():
    return render_template('index.html')

    
@app.route('/register/', methods=['GET','POST'])

def register():
   
    if request.method =="POST" and 'username' in request.form and 'email' in request.form and 'password' in request.form:

        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        con =get_connection()
        con.execute('insert into user(username,email,password) values(?,?,?)',(username,email,generate_password_hash(password)) )
        con.commit()
        con.close()
        return redirect(url_for('login'))
       
       
    return render_template('inscription.html')
    
    
@app.route('/login/',methods=['GET','POST'])
def  login():
    conn = get_connection()
    
    if request.method =="POST": 

        email = request.form['email']
        password = request.form['password']
        
       

        error = None
        user = conn.execute(
        'SELECT * FROM user WHERE email = ?', (email,)
        ).fetchone()
        if user is None:

           error = 'Incorrect email.'
        elif not check_password_hash(user['password'],password):

            error = 'Incorrect password.'
            
       

        elif error is None:
            session.clear()
           
            return render_template('acceuil.html')
           
        flash(error)
        
    
    return render_template('connection.html')     
     

   
     

      

if __name__ =='__main__':

    app.config.update(ENV="development", DEBUG=True)

    app.run()    