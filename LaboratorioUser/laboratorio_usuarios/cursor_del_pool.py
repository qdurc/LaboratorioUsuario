from conexión import Conexion
from logger_base import log

class CursorDelPool:
    def __init__(self):
        self.conn = None
        self.cursor = None
    
    def __enter__(self):
        self.conn = Conexion.obtenerConexion()
        self.cursor = self.conn.cursor()
        return self.cursor
    
    def __exit__(self, tp_excepcion, vl_excepcion, dtlle_excepcion ):
        if vl_excepcion:
            self.conn.rollback()
            log.error(f'Ocurrió una excepcion, se hace rollback: {vl_excepcion} {tp_excepcion} {dtlle_excepcion}')
        else:
            self.conn.commit()
            log.debug(f'Commit de la transaccion')
        self.cursor.close()
        Conexion.liberarConexion(self.conn)
    
# with CursorDelPool() as cursor:
#     cursor.execute('SELECT * FROM usuario')
#     log.debug(cursor.fetchall())