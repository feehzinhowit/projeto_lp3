from flask import Flask, render_template



app = Flask("minha app")


# rota + função

# / - home page
@app.route("/")
def home ():
    return render_template("home.html")

# /contato - pagina de contato
@app.route("/contato")
def contato():
    return render_template("contato.html")


# /produtos - pagina de produos 
@app.route("/produtos")
def produtos():
    lista_produtos = [
        { "nome": "Coca-cola", "descricao": "mata a sede" },
        { "nome": "Doritos", "descricao": "Suja a mão" },
        { "nome": "Chocolate", "descricao": "Bom" }
    ]
    return render_template("produtos.html", produtos=lista_produtos)