import usuarios.conexion as conexion
import datetime
import hashlib

connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

class Usuario:

    def __init__(self,nombre,apellidos,email,password):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.password = password

    def registrar(self):
        fecha = datetime.datetime.now()
        #Cifrar contraseña
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))
        sql = "INSERT INTO usuarios VALUES(null, %s,%s,%s,%s,%s)"
        try:
            usuario_reg = (self.nombre,self.apellidos,self.email,cifrado.hexdigest(),fecha)
            cursor.execute(sql,usuario_reg) 
            database.commit()
            result = [cursor.rowcount, self]
        except:
            result = [0,self]
        return result 
        

    def identificar(self):
        pass 