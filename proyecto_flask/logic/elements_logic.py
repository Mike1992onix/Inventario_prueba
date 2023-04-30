from database.conexion_bd import ConexionBD
from models.elements import elements
class elements_logic:
    conexion = ConexionBD(usuario='root', contrasena='', host='localhost', base_datos='inventario')
    #CREATE ELEMENT
    @classmethod
    def create_elements(cls, element):
        try:
            cursor = elements_logic.conexion.conectar()
            sql = """INSERT INTO elementos(referencia, nombres, cantidad, valor,estado, lugar,fecha_reg,hora_reg,observaciones, ID_categorias) 
                    VALUES ('{}', '{}', {}, {}, '{}', '{}', '{}', '{}', '{}', '{}' )""".format(element.referencia, element.nombres, element.cantidad, element.valor, element.estado, element.lugar, element.fecha_reg, element.hora_reg, element.Observaciones, element.ID_categorias)
            cursor.execute(sql)
            elements_logic.conexion.cnx.commit()
            cursor.close()
            elements_logic.conexion.cerrar()
            return True
        except Exception as ex:
            raise Exception(ex)
        
    #UPDATE ELEMENT
    @classmethod
    def update_elements(cls, element):
        try:
            cursor = elements_logic.conexion.conectar()
            sql = "UPDATE elementos SET nombres='{}', referencia='{}', cantidad='{}', valor='{}', estado='{}', lugar='{}', Observaciones='{}', ID_categorias='{}' WHERE ID_elemento='{}'".format(element.referencia, element.nombres, element.cantidad, element.valor, element.estado, element.lugar, element.Observaciones, element.ID_categorias, element.ID_elemento)
            cursor.execute(sql)
            elements_logic.conexion.cnx.commit()
            elements_logic.conexion.cerrar()
            return True
        except Exception as ex:
            raise Exception(ex)

    #Query the element provided by the user
    @classmethod
    def read_elements(cls, id):
        try:
            cursor = elements_logic.conexion.conectar()
            sql = "SELECT * FROM elementos WHERE ID_elemento='{}'".format(id)
            cursor.execute(sql)
            result = cursor.fetchone()
            elements_logic.conexion.cerrar()
            if result != None:
                newElement = elements(result[0],result[1], result[2], result[3],str(result[4]), result[5],result[6],str(result[7]),str(result[8]), result[9],result[10])
            return newElement
        except Exception as e:
             raise Exception(e)
    
    #DELETE THE CATEGORY FROM THE TABLE categorias
    @classmethod
    def delete_elements(cls, id):
        try:
              cursor = elements_logic.conexion.conectar()
              sql = "DELETE FROM elementos WHERE ID_elemento='{}'".format(id)
              cursor.execute(sql)
              elements_logic.conexion.cnx.commit()
              elements_logic.conexion.cerrar()
              return True
        except Exception as e:
            raise Exception(e)

    @classmethod
    def get_all_elements(cls):
        try:
            cursor = elements_logic.conexion.conectar()
            sql = "SELECT * FROM elementos"
            cursor.execute(sql)
            results = cursor.fetchall()
            cursor.close()
            elements_list = []
            for result in results:
                 Newelement = elements(result[0],result[1], result[2], result[3],str(result[4]), result[5],result[6],str(result[7]),str(result[8]), result[9],result[10])
                 elements_list.append(Newelement)
            return elements_list
        except Exception as e:
            raise Exception(e)

  

    #VERIFY IF THE CATEGORY ALREADY EXISTS IN THE TABLE
    @classmethod
    def exists_elements(cls, id):
        
        try:
            cursor = elements_logic.conexion.conectar()
            sql = "SELECT * FROM elementos WHERE ID_elemento='{}'".format(id)
            cursor.execute(sql)
            result = cursor.fetchone()
            cursor.close()
            if result:
                return True
            else:
                return False
        except Exception as ex:
            raise Exception(ex)
    

