from flask import Flask, request, make_response, jsonify
from flask_cors import CORS
from models.User import usuario
from models.category import category
from models.elements import elements
from models.elemets_dto import elemets_dto
from logic.user_logic import user_login
from logic.category_logic import category_logic
from logic.elements_logic import elements_logic
import json
from datetime import date, datetime
app = Flask(__name__)
CORS(app)
CORS(app, origins="http://127.0.0.1:5500")
CORS(app, resources={r"/api/*": {"origins": "http://localhost:5500"}})


@app.route('/login', methods=["POST"])
def login():
    user = usuario(1, "", request.json["usuario"],
                   request.json["contraseña"], "", "")
    usuario_logeado = user_login.login(user)
    if usuario_logeado == False:
        return make_response("Usuario Invalido o Contraseña Incorrecta", 400)
    elif usuario_logeado == True:
        return make_response("Usuario logueado correctamente", 200)
    elif (usuario_logeado == None):
        return make_response("Usuario no encontrado", 404)


@app.route('/registro', methods=["POST"])
def registro():
    Id = request.json['Documento']
    Nombre = request.json['Nombre']
    Usuario = request.json['usuario']
    password = request.json['contraseña']
    email = request.json['email']
    Observaciones = request.json['Observaciones']
    if not Id or not Nombre or not Usuario or not password or not email or not Observaciones:
        return make_response("Falta Informacion", 400)
    existencia_usuario = user_login.login(
        user=usuario(None, None, Usuario, password, None, None))
    if existencia_usuario is not None:
        return make_response("Usuario ya registrado", 400)
    nuevo_usuario = usuario(Id, Nombre, Usuario,
                            password, email, Observaciones)
    success = user_login.make_user(nuevo_usuario)
    if success:
        return make_response("Usuario creado correctamente", 201)
    else:
        return make_response("ha ocurrido un error", 400)


@app.route('/elements/create', methods=["POST"])
def create_elements():
    hora_actual = datetime.now()
    referencia = request.json["referencia"]
    nombres = request.json["nombres"]
    cantidad = request.json["cantidad"]
    valor = request.json["valor"]
    estado = request.json["estado"]
    lugar = request.json["lugar"]
    fecha_reg = date.today()
    hora_reg = hora_actual.strftime('%H:%M:%S')
    Observaciones = request.json["Observaciones"]
    id_categoria = request.json["id_categoria"]
    if not referencia or not nombres or not cantidad or not valor or not estado or not lugar or not Observaciones:
        return make_response("Falta Informacion", 400)
    existe_elements = elements_logic.exists_elements(nombres)
    if existe_elements == True:
        return make_response("ya existe el elemento", 400)
    new_element = elements('', referencia, nombres, cantidad, valor,
                           estado, lugar, fecha_reg, hora_reg, Observaciones, id_categoria)
    success = elements_logic.create_elements(new_element)
    if success:
        return make_response("elemento creado satisfactoriamente", 201)
    else:
        return make_response("ha ocurrido un error", 400)


@app.route('/category/create', methods=["POST"])
def create_category():
    codigo = request.json["codigo"]
    nombre = request.json["nombre"]
    descripcion = request.json["descripcion"]
    observacion = request.json["observacion"]
    if not codigo or not nombre or not descripcion or not observacion:
        return make_response("Faltan Informacion", 400)
    existe_category = category_logic.exists_category(codigo)
    if existe_category == True:
        return make_response("Ya existe la categoria", 400)
    new_category = category(codigo, nombre, descripcion, observacion)
    success = category_logic.create_category(new_category)
    if success:
        return make_response("Categoria creada correctamente", 201)
    else:
        return make_response("ha ocurrido un error", 400)


@app.route('/elements/update', methods=["PUT"])
def element_update():
    ID_elemento = request.json["id_elemento"]
    referencia = request.json["referencia"]
    nombres = request.json["nombres"]
    cantidad = request.json["cantidad"]
    valor = request.json["valor"]
    estado = request.json["estado"]
    lugar = request.json["lugar"]
    Observaciones = request.json["Observaciones"]
    ID_categorias = request.json["ID_categorias"]
    if not referencia or not nombres or not cantidad or not valor or not estado or not lugar or not Observaciones or not ID_categorias:
        return make_response("Falta Informacion", 400)
    existe_element = elements_logic.exists_elements(ID_elemento)
    if existe_element == False:
        return make_response("Elemento no existe", 404)
    update_element = elemets_dto(ID_elemento, referencia, nombres,
                                 cantidad, valor, estado, lugar, Observaciones, ID_categorias)
    success = elements_logic.update_elements(update_element)
    if success:
        return make_response("Elemento modificado correctamente", 200)
    else:
        return make_response("ha ocurrido un error", 400)


@app.route('/category/update', methods=["PUT"])
def category_update():

    codigo = request.json["codigo"]
    nombre = request.json["nombre"]
    descripcion = request.json["descripcion"]
    observacion = request.json["observacion"]
    if not codigo or not nombre or not descripcion or not observacion:
        return make_response("Faltan Informacion", 400)
    existe_category = category_logic.exists_category(codigo)
    if existe_category == False:
        return make_response("categoria no existe", 404)
    update_category_cero = category(codigo, nombre, descripcion, observacion)
    success = category_logic.update_category(update_category_cero)
    if success:
        return make_response("Categoria modificada correctamente", 200)
    else:
        return make_response("ha ocurrido un error", 400)


@app.route('/elements/delete/<int:id>', methods=["DELETE"])
def elements__delete(id):
    if not id:
        return make_response("Falta Informacion", 400)
    existe_elements = elements_logic.exists_elements(id)
    if existe_elements == False:
        return make_response("elemento no existe", 404)
    success = elements_logic.delete_elements(id)
    if success:
        return make_response("elemento eliminada correctamente", 200)
    else:
        return make_response("ha ocurrido un error", 400)


@app.route('/category/delete/<int:codigo>', methods=["DELETE"])
def category_delete(codigo):
    if not codigo:
        return make_response("Falta informacion", 400)
    existe_category = category_logic.exists_category(codigo)
    if existe_category == False:
        return make_response("categoria no existe", 404)
    success = category_logic.delete_category(codigo)
    if success:
        return make_response("Categoria eliminada correctamente", 200)
    else:
        return make_response("ha ocurrido un error", 400)


@app.route('/elements/read/<int:id>', methods=["GET"])
def element_read(id):

    if not id:
        return make_response("Falta informacion", 400)
    existe_elements = elements_logic.exists_elements(id)
    if existe_elements == False:
        return make_response("elemenot no existe", 404)
    elementoBd = elements_logic.read_elements(id)
    elemento_dict = vars(elementoBd)
    elemento_json = json.dumps(elemento_dict)
    return make_response(elemento_json, 200)


@app.route('/category/read/<int:codigo>', methods=['GET'])
def category_read(codigo):
    if not codigo:
        return make_response("Falta informacion")
    existe_category = category_logic.exists_category(codigo)
    if existe_category == False:
        return make_response("categoria no existe")
    categoryBd = category_logic.read_category(codigo)
    catego_dict = vars(categoryBd)
    category_json = json.dumps(catego_dict)
    return make_response(category_json, 200)


@app.route('/getAllCategories', methods=['GET'])
def get_all_categories():
    categories = category_logic.read_all_categories()
    if categories:
        categories_dict = []
        for category in categories:
            category_dict = vars(category)
            categories_dict.append(category_dict)
        categories_json = json.dumps(categories_dict)
        return make_response(categories_json, 200)
    else:
        return make_response("No existen categorias",  404)


@app.route('/getAllElements', methods=['GET'])
def get_all_elements():
    elements_list = elements_logic.get_all_elements()
    if elements_list:
        elements_dict = []
        for element in elements_list:
            element_dict = vars(element)
            elements_dict.append(element_dict)
        elementes_json = json.dumps(elements_dict)
        return make_response(elementes_json, 200)
    else:
        return make_response("No existen elementos",  404)


if __name__ == '__main__':
    app.run(debug=True)
