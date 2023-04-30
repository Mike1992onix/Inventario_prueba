from models.User import usuario
from database.conexion_bd import ConexionBD

class user_login():
    conexion = ConexionBD(usuario='root', contrasena='', host='localhost', base_datos='inventario')

    @classmethod
    def login(self, user):
            try:
                cursor = user_login.conexion.conectar()
                sql="""SELECT * FROM usuario 
                            WHERE Usuario = '{}'""".format(user.Usuario) # se realiza la consulta a la base de datos para encontrar el usuario apartir email
                cursor.execute(sql)
                row = cursor.fetchone()
                print(row)
                if row != None:
                    newUser = usuario(row[0], row[1], row[2], row[3], row[4], row[5],) #hace la validacion de la contraseña para hacer el login
                    verificacion_pass = newUser.verificar_password(user.password, newUser.password) 
                    return verificacion_pass
                else:   
                    return None
            except Exception as ex:
                    raise Exception(ex)
            

    @classmethod
    def make_user(cls,user):
        try:
            cursor = user_login.conexion.conectar()
            sql=""" INSERT INTO usuario(ID,Nombre, Usuario, password, email, Observaciones) 
            VALUES ('{}','{}','{}','{}','{}','{}')""".format(user.ID,user.Nombre,user.Usuario,user.password,user.email,user.Observaciones)
            cursor.execute(sql)
            user_login.conexion.cnx.commit()
            #mybd.close()
            return True
        except Exception as ex:
                    raise Exception(ex)
        
    