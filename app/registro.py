# app/registro.py

def registrar_usuario(nombre):
    if not nombre:
        return "Nombre inválido"
    return f"Usuario {nombre} registrado"
