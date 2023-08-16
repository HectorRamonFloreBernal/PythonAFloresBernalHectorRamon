from faker import Faker

from  reportes311.models import Supplier

#faker = Faker()
fake = Faker(['it_IT', 'en_US', 'es_ES','es_MX'])

class SupplierSolicitud:
    
    def build_supplier_JSON(self):
        return{
           'idSolicitud' : str(fake.random_number(digits=11)),
           'fechaSolicitud' : fake.date_of_birth(),
           'idUsuario' : fake.company(),
           'descripcion' : fake.name(),       
           'fotoUbicacion' : fake.name(),
           'direccionIncidente' :fake.address(),
           'status' : fake.name(),
           'idSeguimiento' : str(fake.random_number(digits=11))
        }
      
    
    def createSupplier(self):
        return Supplier.objects.create(**self.build_supplier_JSAny)
        