from flask import Flask, render_template, request
from validate_docbr import CPF, CNPJ

lista_produtos = [
        { "nome": "Coca-cola", "descricao": "mata a sede" },
        { "nome": "Doritos", "descricao": "Suja a mão" },
        { "nome": "Chocolate", "descricao": "Bom" }
]

app = Flask("minha app")


# rota + função

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
    return render_template("produtos.html", produtos=lista_produtos)

@app.route("/termosdeuso")
def termosDeUso():
    return render_template("termosDeUso.html")


@app.route("/politicadeprivacidade")
def politicasDePrivacidade():
    return render_template("politicaDePrivacidade.html")


@app.route("/comoutilizar")
def comoUtilizar():
    return render_template("comoUtilizar.html")

# GET /produtos/cadastro devolver o form
@app.route("/produtos/cadastro")
def cadastro_produtos():
    return render_template("cadastro_produtos.html")


# POST /produtos que vai validar com os dados enviados pelo form
# enviados pelo form
#acessar o objeto request

@app.route("/produtos", methods=['POST'])
def salvar_produtos():

    # pegando os valores digitados no form
    # que estao na request
    nome = request.form["nome"]
    descricao = request.form["descricao"]

    # crio um novo produto (novo dicionario)
    produto = {"nome": nome, "descricao": descricao}

    # adiciona o novo produto na lista 
    lista_produtos.append(produto)

    # devolvo o template com o novo produto
    return render_template("produtos.html", produtos=lista_produtos)