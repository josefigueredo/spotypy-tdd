import unittest
from user import User
from spotipy import Spotipy
from not_available_email import NotAvailableEmail

class UserRegisterTestCase(unittest.TestCase):

    def setUp(self):
        self.__spotipy = Spotipy()
        self.__pepe_email = "jose_perez@gmail.com"
        self.__pepe_name = "Jose"
        self.__pepe_last_name = "Perez"
        self.__new_user_pepe = User(self.__pepe_email, self.__pepe_name, self.__pepe_last_name)

    def test_usuario_sin_cuenta_se_registra_con_mail_disponible(self):

        self.__spotipy.register_user(self.__new_user_pepe)

        expectedResponse = self.__spotipy.is_registered(self.__pepe_email)

        self.assertTrue(expectedResponse)

    def test_usuario_se_registra_con_email_duplicado_lanza_excepcion(self):
        self.__spotipy.register_user(self.__new_user_pepe)
        self.assertRaises(NotAvailableEmail, lambda: self.__spotipy.register_user(self.__new_user_pepe))

if __name__ == "__main__":
    unittest.main()
