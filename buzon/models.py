from django.db import models

class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre_tipo = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_tipo

class Mensaje(models.Model):
    id_escrito = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='imagenes/', blank=True, null=True)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo