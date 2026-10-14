from flask import Flask ,render_template
app = Flask(__name__)

@app.route('/')
def index():
    titulo="PWA"
    lista=["limon","Binboro","Gato"]
    return render_template("index.html",titulo=titulo,lista=lista)

@app.route('/hola')
def func():
    return "Olaaa"

@app.route('/user/<string:user>')
def user(user):
   return "hola  " + user

@app.route('/numero/<int:n>')
def numero(n):
   return "numero:  {}".format(n)


@app.route('/user/<int:id>/<string:username>')
def username(id,username):
   return "ID: {} Nombre {}".format(id,username)


@app.route('/suma/<float:n1>/<float:n2>')
def suma(n1,n2):
   return "Lasuma:  {}".format(n1+n2)



if __name__=="__main__":
    app.run(debug=True)

