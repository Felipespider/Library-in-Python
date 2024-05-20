# API: lUGAR PARA DISPOBLIZAR RECURSOS OU FUNCIOINALIDADES
# Objetivo - Criar Uma API que disponibiliza a consulta, criação e edição de livros
#  URL BASE - localhost.com - 
#   EndPoints - LocalHost/livros (GET) || -LocalHost/livros/id (GET, livros específicos) || LocalHost/livros/id (PUT) || localhost/livros/id (DELETE)
#  Quais Recursos - Livros

from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'título': 'O Senhor dos Anéis - A Sociedade do Anel',
        'autor': 'J.R.R Tolkien'
    },
    
    {
        'id': 2,
        'título': 'Harry Potter e a Pedra Filosofal',
        'autor': 'J.K Howling'
    },
    
    {
        'id': 3,
        'título': 'James Clear',
        'autor': 'Hábitos Atômicos'
    },
]

#Consultar todos
@app.route('/livros', methods = ["GET"]) #ROTA + EndPoint com o métofdo exclusivo GET seja utilizado para ser acessado os dados do livro
def obter_livros ():
    return jsonify(livros)

#Consultar(id)
@app.route('/livros/<int:id>', methods = ['GET']) #Especificando que o número INTEIRO vai ser a palavra chave ID = <int:id> em forma de ROTA 
def obter_livro_por_id(id): #Entra na propriedade do livro e acessa o id, se o ID como paramêtro for 1, ele irá me retornar o livro de ID1
    for livro in livros:
        if livro.get("id") == id:
            return jsonify(livro) 
        
#Editar
@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro_por_id(id):
   livro_alterado =  request.get_json() #Retornar as informações enviadas pelo usuário para a API
   for indice,livro in enumerate(livros): 
       if livro.get("id") == id:
           livros[indice].update(livro_alterado) #Se o ID do livro que o usuário escolheu alterar for igual ao id do próprio livro enumerado, será realizado o update do livro agora editado
           return jsonify(livros[indice])

#Criar
@app.route('/livros', methods =['POST'])
def incluir_novo_livro():
    novo_livro = request.get_json() #request.get_json() = Receber a informação que o usuário irá depositar (quase igual a input)
    livros.append(novo_livro)
    
    return jsonify(livros) 

#Excluir
@app.route('/livros/<int:id>',methods=['DELETE'])
def excluir_livro(id): #Recebe o ID como paramêtro colocado na rota
    for indice, livro in enumerate(livros): #Enumera os livros pelo indice, id e livro
        if livro.get("id") == id:
            del livros[indice]
            
    return jsonify(livros)
            
app.run(port=5000, host = 'localhost', debug = 'True')