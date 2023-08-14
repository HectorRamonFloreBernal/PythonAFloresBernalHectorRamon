from django.db import models


# Create your models here.

#--------------  Clase de solicitud
class Solicitud(models.Model):
    idSolicitud = models.IntegerField(verbose_name="Id Solicitud")
    fechaSolicitud = models.DateTimeField()
    idUsuario = models.CharField(verbose_name="IDUsuario", max_length=200)
    descripcion = models.CharField(verbose_name="Descipción", max_length=200)
    fotoUbicacion= models.ImageField(upload_to='imagenes/', null=True)
    direccionIncidente = models.CharField( max_length=100)
    status = models.CharField(max_length=20)
    idSeguimiento = models.IntegerField(null=True)
     
    def __str__(self):
        fila = "No Solicitud: "  + str(self.idSolicitud) + " / Fecha:  " + str(self.fechaSolicitud) + " /  No Usuario: " + str(self.idUsuario) +  " / Descipcion: " + str(self.descripcion) + " / Ubiación: " + str(self.fotoUbicacion) + " / Dirección: " + str(self.direccionIncidente) + " / Estatus:  " + str(self.status) + " / No Seguimeinto:  " + str(self.idSeguimeinto)
        # fila = "No Solicitud: "  + str(self.idSolicitud) + " / Fecha:  " + str(self.fechaSolicitud) + " /  No Usuario: " + str(self.idUsuario) +  " / Descipcion: " + str(self.descripcion) + " / Ubiación: " + str(self.fotoUbicacion) + " / Dirección: " + str(self.direccionIncidente) + " / Estatus:  " + str(self.status) + " / No Seguimeinto:  "
        return fila
     
    def delete(self, using=None, keep_parents=False):
        self.fotoUbicacion.storage.delete(self.fotoUbicacion.name)
        super().delete()
        
     # idUsuario = models.IntegerField()   
        
 #--------------- Clase de Seguimiento ----------------------       
class Seguimiento(models.Model):
   
    idUsuario = models.CharField(verbose_name="IdUsuario", max_length=200)
    idSolicitud = models.IntegerField(verbose_name="Id Solicitud")
    fechaSeguimiento = models.DateTimeField()
    descripcionSeguimiento = models.CharField(verbose_name="Descipción", max_length=200)
    
    def __str__(self):
         fila = "Usuario: " + str(self.idUsuario) + " / Solicitud:  " + str(self.idSolicitud) + " / Fecha:  " + str(self.fechaSeguimiento) +  " / Descipcion: " + str(self.descripcionSeguimiento)
         return fila
    
    # idSeguimiento = models.AutoField(primary_key=True)
    # idSolicitud = models.ForeignKey(Solicitud,on_delete=models.CASCADE,related_name="FK_Solicitud_Seguimiento")
    
    
    
    
    #--------------- usuario
    
#class Usuario(AbstractBaseUser, PermissionsMixin):
 #       username = models.CharField('Nombre de Usuario', unique = True, max_length = 100)
  #      email = models.CharField('Correo Electronico', max_length = 254, unique = True)
   #     nombres= models.CharField('Nombres', max_length = 200, blank=True, null = True)
    #    apellidos= models.CharField('Apellidos', max_length = 200, blank=True, null = True)
    #    rol= models.CharField(Rol, on_delete=models.CASCADE, blank=True, null = True)
     #   imagen= models.ImagenField('Imagen de Perfil', upload_to='perfil/', max_length = 200, blank=True, null = True)
      #  is_active = models.BooleanField(default= True)
       # is_staff = models.BooleanField(default= False)
       # objets = UsuarioManager()