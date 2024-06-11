from flask import Flask

app = Flask("minha app")


# rota + função

# / - home page
@app.route("/")
def home ():
    return "<h1>Home Page </h1>"

# /contato - pagina de contato
@app.route("/contato")
def contato():
    return "<h1>Contato</h1>"


# /produtos - pagina de produos 
@app.route("/produtos")
def produtos():
    return "<h1>PRODUTOS</h1>"