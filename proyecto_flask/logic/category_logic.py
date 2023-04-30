from models.category import category
from database.conexion_bd import ConexionBD

class category_logic():

    conexion = ConexionBD(usuario='root', contrasena='', host='localhost', base_datos='inventario')
    #CREATE CATEGORY
    @classmethod
    def create_category(cls,category):
        
        try:
            cursor = category_logic.conexion.conectar()
            sql=""" INSERT INTO categorias(codigo, nombre, descripcion, observacion) 
            VALUES ('{}','{}','{}','{}')""".format(category.codigo, category.nombre, category.descripcion, category.observacion)
            cursor.execute(sql)
            category_logic.conexion.cnx.commit()
            cursor.close()
            category_logic.conexion.cerrar()
            return True
        except Exception as ex:
                raise Exception(ex)
        
    #UPDATE CATEGORY
    @classmethod
    def update_category(cls, category):
        try:
            cursor = category_logic.conexion.conectar()
            sql = "UPDATE categorias SET nombre='{}', descripcion='{}', observacion='{}' WHERE codigo='{}'".format(category.nombre, category.descripcion, category.observacion, category.codigo)
            cursor.execute(sql)
            category_logic.conexion.cnx.commit()
            category_logic.conexion.cerrar()
            return True
        except Exception as ex:
            raise Exception(ex)

    #Query the category provided by the user
    @classmethod
    def read_category(cls, codigo):
        try:
            cursor = category_logic.conexion.conectar()
            sql = "SELECT * FROM categorias WHERE codigo='{}'".format(codigo)
            cursor.execute(sql)
            result = cursor.fetchone()
            cursor.close()
            if result != None:
                newCategory = category(result[1], result[2], result[3],result[4])
            return newCategory
        except Exception as e:
             raise Exception(e)

    @classmethod
    def read_all_categories(cls):
        try:
            cursor = category_logic.conexion.conectar()
            sql = "SELECT * FROM categorias"
            cursor.execute(sql)
            results = cursor.fetchall()
            cursor.close()
            categories = []
            for result in results:
                New_category = category(result[1], result[2], result[3], result[4])
                categories.append(New_category)
            return categories
        except Exception as e:
            raise Exception(e)


    
    #DELETE THE CATEGORY FROM THE TABLE categorias
    @classmethod
    def delete_category(cls, codigo):
        try:
              cursor = category_logic.conexion.conectar()
              sql = "DELETE FROM categorias WHERE codigo='{}'".format(codigo)
              cursor.execute(sql)
              category_logic.conexion.cnx.commit()
              category_logic.conexion.cerrar()
              return True
        except Exception as e:
            raise Exception(e)


  

    #VERIFY IF THE CATEGORY ALREADY EXISTS IN THE TABLE
    @classmethod
    def exists_category(cls, codigo):
        
        try:
            cursor = category_logic.conexion.conectar()
            sql = "SELECT * FROM categorias WHERE codigo='{}'".format(codigo)
            cursor.execute(sql)
            result = cursor.fetchone()
            cursor.close()
            if result:
                return True
            else:
                return False
        except Exception as ex:
            raise Exception(ex)
    