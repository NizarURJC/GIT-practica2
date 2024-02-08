#!/usr/bin/python
# -*- coding: utf-8 -*-

# Ruta al archivo /etc/passwd
ruta_passwd = '/etc/passwd'

# Verificar si el archivo existe antes de intentar abrirlo
try:
    with open(ruta_passwd, 'r') as archivo_passwd:
        # Leer todas las líneas del archivo y almacenarlas en una lista
        lineas_passwd = archivo_passwd.readlines()

        # Crear una lista para almacenar identificadores de usuario y sus shells
        usuarios_shells = []

        # Iterar sobre cada línea del archivo
        for linea in lineas_passwd:
            # Dividir la línea en campos usando ':' como delimitador
            campos = linea.split(':')

            # Obtener el identificador de usuario y la shell asociada
            usuario = campos[0]
            shell = campos[-1].strip()  # Eliminar el salto de línea al final

            # Agregar una tupla (usuario, shell) a la lista
            usuarios_shells.append((usuario, shell))

        # Imprimir la shell asociada a cada identificador de usuario
        for usuario, shell in usuarios_shells:
            print(f'Usuario: {usuario}, Shell: {shell}')

        # Imprimir el número total de usuarios utilizando el método asociado a la lista
        numero_usuarios = len(usuarios_shells)
        print(f'\nNúmero total de usuarios: {numero_usuarios}')

except FileNotFoundError:
    print(f'El archivo {ruta_passwd} no existe.')
except Exception as e:
    print(f'Ocurrió un error: {e}')
