import py_compile
from flask import Flask, render_template, request
from requests import post
from flask_mysqldb import MySQL


app = Flask(__name__)

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "acfull"

mysql = MySQL(app)

@app.route('/', methods=['GET','POST'])
def index():

  if request.method == 'POST':
       nome = request.form['nome']
       email = request.form['email']
       endereco = request.form['endereco']

       cur = mysql.connection.cursor()

       cur.execute( "INSERT INTO users (nome, email, endereco) VALUES (%s,%s,%s)" (nome, email, endereco))

       mysql.connection.commit()
       cur.close()
       return "sucess"

     return render_template('index.html')    

@app.route('/users') 
def users():
    cur = mysql.connection.cursor()
    users = cur.execute("SELECT * FROM users")
    if users > 0:
      userDetails = cur.fetchall()

       return render_template('users.html', userDetails=userDetails)



if __name__ == "__main__":
    app.run(debug=True)   



