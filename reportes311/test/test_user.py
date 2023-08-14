import pytest
from proyecto311.reportes311.models import Usuario

def test_user_creation():
    user = Usuario.objects.create_user(
        
        username = 'hector'
        email = 'flores@tecnm.mx'
        password='12345'
    )
    assert user.username == 'hector'
    