from flask import Flask, render_template
from validate_docbr import CPF, CNPJ



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




@app.route("/cpf")
def cpf():
    cpf = CPF()
    GerarCpf = cpf.generate(True)
    return render_template("cpf.html", cpf = GerarCpf)



@app.route("/cnpj")
def cnpj():
    cnpj = CNPJ()
    GerarCnpj = cnpj.generate(True)
    return render_template("cnpj.html", cnpj = GerarCnpj)


@app.route("/termosdeuso")
def termosDeUso():
    return render_template("termosDeUso.html")


@app.route("/politicadeprivacidade")
def politicasDePrivacidade():
    return render_template("politicaDePrivacidade.html")


@app.route("/comoutilizar")
def comoUtilizar():
    return render_template("comoUtilizar.html")