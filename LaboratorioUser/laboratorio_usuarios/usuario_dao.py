from cursor_del_pool import CursorDelPool
from usuario import Usuario
from logger_base import log

class UsuarioDao:
    'DAP = Data Acces Object'
    _SELECCIONAR = 'SELECT * FROM usuario ORDER BY id_usuario'
    _INSERTAR = 'INSERT INTO usuario(username, password) VALUES (%s,%s)'
    _ACTUALIZAR = 'UPDATE usuario SET username=%s, password=%s WHERE id_usuario=%s'
    _ELIMINAR = 'DELETE FROM usuario WHERE id_usuario=%s'
    
    @classmethod
    def seleccionar(cls): 
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            usuarios = []
            for registro in registros:
                usuario = Usuario(registro[0], registro[1], registro[2])
                usuarios.append(usuario)
            return usuarios
    
    @classmethod
    def insertar(cls, usuario): 
        with CursorDelPool() as cursor:
            valores = (usuario.username, usuario.password)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'Usuario a insertar: {usuario}')
            return cursor.rowcount
        
    @classmethod
    def actualizar(cls, usuario):
        with CursorDelPool() as cursor:
            valores = (usuario._username, usuario._password, usuario._id_usuario)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'Usuario actualizado: {usuario}')
            return cursor.rowcount
            
    @classmethod
    def eliminar(cls, usuario):
        with CursorDelPool() as cursor:
            valores = (usuario._id_usuario)
            cursor.execute(cls._ELIMINAR, valores)
            log.debug(f'Usuario eliminado: {usuario}')
            return cursor.rowcount

# if __name__ == '__main__':
    # user1 = Usuario(username='jperez',password=123) 
    # user_insertado = UsuarioDao.insertar(user1)
    # log.debug(f'Persona insertada: {user_insertado}')
    
    # user1 = Usuario(3,'kgomez', 456)
    # user_actualizado = UsuarioDao.actualizar(user1)
    # log.debug(f'Usuario actualizado: {user_actualizado}')
    
    # usuarios = UsuarioDao.seleccionar()
    # for usuario in usuarios:
    #     print(usuario)