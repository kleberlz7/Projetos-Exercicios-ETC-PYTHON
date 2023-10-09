from flask import Flask, jsonify, request

app = Flask(__name__)

episodios = [
{
    'id':1,
    'título': 'S1-E1 - Cachorro e Motosserra'
},
{
    'id':2,
    'título': 'S1-E2 - Chegada em Tokyo'
},
{
    'id':3,
    'título': 'S1-E3 - O Paradeiro de Miauzin'
},
{
    'id':4,
    'título': 'S1-E4 - Resgate'
},
{
    'id':5,
    'título': 'S1-E5 - O Demônio da Arma'
},
{
    'id':6,
    'título': 'S1-E6 - Matem o Denji'

},
{
    'id':7,
    'título': 'S1-E7 - O Sabor do Beijo'
},
{
    'id':8,
    'título': 'S1-E8 - O Som do Disparo'
},
{
    'id':9,
    'título': 'S1-E9 - De Kyoto'
},
{
    'id':10,
    'título': 'S1-E10 - Ainda Mais Podre'
},
{
    'id':11,
    'título': 'S1-E11 - Início do Plano'
},
{
    'id':12,
    'título': 'S1-E12 - Katana vs. Motosserra'
},

]
@app.route('/episodios',methods=['GET'])
def obter_episodios():
    return jsonify(episodios)


@app.route('/episodios/<int:id>',methods=['GET'])
def obter_episodio_por_id(id):
    for episodio in episodios:
        if episodio.get('id') == id:
            return jsonify(episodio)
        
@app.route('/episodios/<int:id>',methods=['PUT'])
def editar_episodio_por_id(id):
    episodio_alterado = request.get_json()
    for indice,episodio in enumerate(episodios):
        if episodio.get('id') == id:
            episodios[indice].update(episodio_alterado)
            return jsonify(episodios[indice])

@app.route('/episodios',methods=['POST'])        
def incluir_novo_episodio():
    novo_episodio = request.get_json() 
    episodios.append(novo_episodio)

    return jsonify(episodios) 
      
@app.route('/episodios/<int:id>',methods=['DELETE'])
def excluir_episodio(id):
    for indice, episodio in enumerate(episodios):
        if episodio.get('id') == id:
            del episodios[indice]
    return jsonify(episodios)            

app.run(port=5000,host='localhost',debug=True)
