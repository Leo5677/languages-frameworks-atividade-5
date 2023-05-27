# IMPORTO TODOS OS MÓDULOS DO FLASK
from flask import *

# CONFIGURAÇÕES DO FLASK PARA ACEITAR TEMPLATE
app = Flask(__name__, template_folder="./")

# ROTA PARA RENDEREIZAÇÃO DO TEMPLATE
@app.route("/", methods=["GET"])
def carregarForm():
    return render_template("form_imc.html")

# ROTA PARA CALCULAR O IMC APÓS O SUBMIT DO FORMULÁRIO
@app.route("/calcular_imc", methods=["GET", "POST"])
def calcularIMC():
    # VERIFICA O VALOR DIGITADO
    altura = float(request.form.get("altura"))
    peso = float(request.form.get("peso"))
    imc = float("{:.2f}".format(peso / (altura ** 2)))
    
    # CATEGORIZA O IMC
    if(imc < 18.5): 
      imc_categoria = "Magreza"
    elif (imc >= 18.5 and imc <= 24.9): 
      imc_categoria = "Normal"
    elif (imc >= 24.9 and imc <= 30):
      imc_categoria = "Sobrepeso"
    else :
      imc_categoria = "Obesidade"
      
    return f"{imc_categoria} -> Seu IMC é de: {imc}" 

# EXECUÇÃO DO APP, PASSANDO AS CONFIGURAÇÕES DE REDE E DEBUG
app.run(host="localhost", port=8080, debug=True)
