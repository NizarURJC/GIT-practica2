#!/usr/bin/python
# -*- coding: utf-8 -*-

# Importar la biblioteca os para manejar archivos y directorios
import os

# Ruta al archivo /etc/passwd
ruta_passwd = '/etc/passwd'

# Verificar si el archivo existe antes de intentar abrirlo
if os.path.exists(ruta_passwd):
    # Abrir el archivo en modo lectura
    with open(ruta_passwd, 'r') as archivo_passwd:
        # Leer todas las líneas del archivo y almacenarlas en una lista
        lineas_passwd = archivo_passwd.readlines()

        # Crear un diccionario para almacenar identificadores de usuario y sus shells
        usuarios_shells = {}

        # Iterar sobre cada línea del archivo
        for linea in lineas_passwd:
            # Dividir la línea en campos usando ':' como delimitador
            campos = linea.split(':')

            # Obtener el identificador de usuario y la shell asociada
            usuario = campos[0]
            shell = campos[-1].strip()  # Eliminar el salto de línea al final

            # Almacenar la shell asociada al identificador de usuario en el diccionario
            usuarios_shells[usuario] = shell

        # Imprimir la shell asociada a cada identificador de usuario
        for usuario, shell in usuarios_shells.items():
            print(f'Usuario: {usuario}, Shell: {shell}')

        # Imprimir el número total de usuarios
        numero_usuarios = len(usuarios_shells)
        print(f'\nNúmero total de usuarios: {numero_usuarios}')

else:
    print(f'El archivo {ruta_passwd} no existe.')
