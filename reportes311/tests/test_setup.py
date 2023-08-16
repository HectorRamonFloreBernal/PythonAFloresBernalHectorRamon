# permite realizar las pruebas unitarias
from rest_framework.test import APITestCase
from rest_framework import status
from faker import Faker

# ------------------------  Clase para creacion de test de usuario ---------------------
class TestSetup(APITestCase):
    
    def setUP(self):
        
        from proyecto311 import User
        # permite crear informacion ficticia para la preba
        faker = Faker()
        
        # ruta de acceso al login
        self.login_url = 'accounts/login/'
        
        # solicitar el usuario
        self.user = User.objects.create_superuser(
            name= 'Developer',
            las_name= 'Developer',
            username= faker.name(),
            password= 'developer',
            email = faker.email()
        )

        # crea un cliente de navecacion para el usuario
        response = self.client.post(
                 self.login_url,
                 {
                     'username' : self.user.username,
                     'password' : 'developer'
                 },
                 format = 'json'
        )
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        import pdb; pdb.set_trace()
        #self.token = response.data['token']
        #self.client.credential(HTTP_AUTHORIZATION='Bearer ' + self.token)
        return super().setUp()
    
    def test_prueba(self):
        pass
        