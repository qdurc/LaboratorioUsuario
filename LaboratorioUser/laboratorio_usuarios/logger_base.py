import logging as log

log.basicConfig(level=log.INFO,
            format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                # asctime = fecha y hora
                # levelname = agrega si fue debug, info etc
                # filename = agrega el nombre del archivo al mensaje
                # lineno = numero de linea al mensaje
                # message = mensaje agregado
            datefmt='%I:%M,%S %p',
                # I = hora
                # M = minutos
                # S = segundos
                # p = AM o PM
            handlers = [
                log.FileHandler('BD/laboratorio_usuarios/laboratorio_usuarios.log'),
                log.StreamHandler()
            ])