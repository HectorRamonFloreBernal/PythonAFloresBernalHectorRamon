from faker import Faker

#from proyecto311 import test 
from django.test import TestCase

#from reportes311.test import APITestCase
from rest_framework.test import APITestCase

from rest_framework import status


class TestSetup(APITestCase):
    def setUp(self):
        from reportes311.models import Solicitud
        faker = Faker()
        self.url = '/solicitudes/crear/'
        self.solicitud = Solicitud.objects.create(
            idSolicitud = faker.random_number(digits=5),
            fechaSolicitud = faker.date_time(),
            idUsuario = faker.random_number(digits=5),
            descripcion = faker.text(),
            fotoUbicacion= faker.image_url(),
            direccionIncidente = faker.address(),
            status = faker.random_number(digits=1),
            idSeguimiento = faker.random_number(digits=5),
        )
            
        
        
        
        response = self.client.post(
            self.url,
           # self.login_url, 
            {
               'username': self.user.username,
               'password': 'developer',
                
            }, 
            format='json'
                
        )
        
        #self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, 200)
        #self.token = response.data['token']
        #self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        return super().setUp()
    
    def test_x(self):
        pass
        
        
   # self.login_url = '/solicitudes/crear/'
       # self.user = Solicitud.objects.create_superuser(
       #     name='Develioper',
       #     last_name='Developer',
        #     username= faker.user_name(),
        #     password='developer',
        #     email=faker.email()
        # )
            
        
                                    