from usuario_dao import UsuarioDao
from cursor_del_pool import CursorDelPool
from usuario import Usuario
from logger_base import log

opcion = None
while opcion != 5:
    try:
        print('''Opciones:
              1) Listar usuario
              2) Agregar usuario
              3) Actualizar usuario
              4) Eliminar usuario
              5) Salir
              ''')
        opcion = int(input('Escribe tu opcion (1-5): '))
        if opcion == 1:
            with CursorDelPool() as cursor:
                usuarios = UsuarioDao.seleccionar()
                for usuario in usuarios:
                    print(usuario)
        elif opcion == 2:
            with CursorDelPool() as cursor:
                user_var = input('Ingrese el usuario: ')
                password_var = input('Ingrese la contraseña: ')
                usuario = Usuario(username=user_var, password=password_var)
                usuarios_insertados = UsuarioDao.insertar(usuario)
                log.info(f'Usuarios insertados: {usuarios_insertados}')
        elif opcion == 3:
            id_usuarios_var = int(input('Escribe el id usuario a modificar: '))
            username_var = input('Escribe el nuevo username: ')
            password_var = input('Escribe el nuevo password: ')
            usuario = Usuario(id_usuarios_var, username_var, password_var)
            usuarios_actualizados = UsuarioDao.actualizar(usuario)
            log.info(f'Usuario actualizado: {usuarios_actualizados}')
        elif opcion == 4:
            id_usuario_var = input('Escribe el id usuario a eliminar: ')
            usuario = Usuario(id_usuario=id_usuario_var)
            usuarios_eliminados = UsuarioDao.eliminar(usuario)
            log.info(f'Usuario eliminado: {usuarios_eliminados}')
        else:
            print('Salimos de la aplicación')
                
    except Exception as e:
        print(e)