from flask import Flask ,render_template,request
app = Flask(__name__)

@app.route('/')
def index():
    titulo="PWA"
    lista=["limon","Binboro","Gato"]
    return render_template("index.html",titulo=titulo,lista=lista)



@app.route("/operasBas",methods=["GET","POST"])
def operasBas():
   n1=0
   n2=0
   res=0
   operacion=''
   if request.method=='POST':
      n1=request.form.get('n1')
      n2=request.form.get('n2')
      if request.form.get('operacion')=='sumar':
         res=float(n1)+float(n2)
         operacion = '+'
      elif request.form.get('operacion')=='restar':
         res=float(n1)-float(n2)
         operacion = '-'

      elif request.form.get('operacion')=='multiplicar':
         res=float(n1)*float(n2)
         operacion = '*'

     


   return render_template("operasBas.html",n1=n1,n2=n2,res=res,operacion=operacion)

@app.route("/distancia", methods=["GET", "POST"])
def distancia():
  Xcord1 = 0
  Xcord2 = 0
  Ycord1 = 0
  Ycord2 = 0
  distancia = 0

  if request.method == "POST":
    Xcord1 = request.form.get("Xcord1")
    Xcord2 = request.form.get("Xcord2")
    Ycord1 = request.form.get("Ycord1")
    Ycord2 = request.form.get("Ycord2")

    distancia = ((float(Xcord1) - float(Xcord2)) ** 2 + (float(Ycord1) - float(Ycord2)) ** 2) ** 0.5

  return render_template(
      "distancia.html",
      Xcord1=Xcord1,
      Xcord2=Xcord2,
      Ycord1=Ycord1,
      Ycord2=Ycord2,
      distancia=distancia,
  )






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

