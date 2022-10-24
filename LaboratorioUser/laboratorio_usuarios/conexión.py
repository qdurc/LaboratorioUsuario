from psycopg2 import pool
from logger_base import log
import sys

class Conexion:
    _DATABASE = 'test_db'
    _USERNAME = 'postgres'
    _PASSWORD = 'edu123'
    _DB_PORT = '5432'
    _HOST = 'localhost'
    _MIN_CON = 1
    _MAX_CON = 5
    _pool = None
    
    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MIN_CON, cls._MAX_CON,
                                                      database=cls._DATABASE,
                                                      user=cls._USERNAME,
                                                      password=cls._PASSWORD,
                                                      port=cls._DB_PORT,
                                                      host=cls._HOST)
                log.debug('Conexion exitosa')
                return cls._pool
            except Exception as e:
                log.error('Error en la conexion')
                print(e)
                sys.exit()
        else:
            return cls._pool
      
    @classmethod
    def obtenerConexion(cls):
        conexion = Conexion.obtenerPool().getconn()
        log.debug('Conexion del pool obtenida')
        return conexion
    
    @classmethod
    def liberarConexion(cls, conexion):
        cls.obtenerPool().putconn(conexion)
        log.debug('Regresamos la conexion al pool')
        
    @classmethod
    def cerrarConexion(cls):
        cls.obtenerPool().closeall()