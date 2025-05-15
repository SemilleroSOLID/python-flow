# tests/test_registro.py
import unittest
from app.registro import registrar_usuario

class TestRegistro(unittest.TestCase):
    def test_registro_valido(self):
        self.assertEqual(registrar_usuario("Ana"), "Usuario Ana registrado")

    def test_registro_invalido(self):
        self.assertEqual(registrar_usuario(""), "Nombre inválido")

if __name__ == '__main__':
    unittest.main()
