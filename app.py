from flask import Flask,render_template,redirect,session,url_for,request

app=Flask(__name__)
app.secret_key="unaclavesecreta"

@app.route("/")
def index():
    if 'usuario' not in session:
        session['usuario']=[]
        return render_template("index.html")
    return render_template("secion.html")

@app.route ("/secion")
def secc():
    return render_template("secion.html")

@app.route("/valida",methods=['POST'])
def valida():

    if request.method == 'POST':
        usuario=request.form.get("usuario")
        contra=request.form.get("contra")
        
        if 'usuario' not in session:
         session['usuario']=[]
        session['usuario'].append({'nombre':usuario,'pass':contra}) 
        session.modified=True
        if(usuario=="Jhovani Salviery" and contra== "12344321"):
            return render_template("secion.html",usuario=session['usuario'])
        else:
            return render_template("error.html")
        
    return render_template("index.html")


@app.route("/cerrar")
def cerra():
    session.pop('usuario',None)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)