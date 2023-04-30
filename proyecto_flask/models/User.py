from werkzeug.security import check_password_hash

class usuario():

    def __init__(self, ID, Nombre, Usuario, password, email, Observaciones) -> None:
        self.ID = ID
        self.Nombre = Nombre
        self.Usuario = Usuario
        self.password = password
        self.email = email
        self.Observaciones = Observaciones
        



    
    def get_id(self):
        return str(self.ID)

    @classmethod
    def check_password(self, hashed_password, password):
        return check_password_hash(hashed_password, password)

    @classmethod
    def verificar_password(self, password, bd_password):
        if password != bd_password:
            return False
        else:
            return True 

