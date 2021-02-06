from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Category(models.Model):
    title= models.CharField(max_length=200, verbose_name= "Categoría")
    
    def __str__(self):
        return self.title 

class Project(models.Model):
    order = models.IntegerField(null=True, blank=True)
    title= models.CharField(max_length=200, verbose_name= "Titulo")
    category= models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    tecnology= models.CharField(max_length=200, verbose_name= "Lenguajes", null=True, blank=True)
    client= models.CharField(max_length=200, verbose_name= "Cliente", null=True, blank=True)
    description= RichTextField(verbose_name= "Descripcion") #acordate de poner contenido safe
    imageOne= models.ImageField(verbose_name= "Imagen principal", upload_to="projects", null=True, blank=True)
    imageTwo= models.ImageField(verbose_name= "Imagen secundaria", upload_to="projects", null=True, blank=True)
    der= models.ImageField(verbose_name= "Diagrama", upload_to="projects", null=True, blank=True)
    dertext= RichTextField(verbose_name= "Explicación Der", null=True, blank=True) #acordate de poner contenido safe
    video = models.FileField(upload_to="videos", null=True, blank=True) 
    git= models.URLField(verbose_name= "Repositorio de Git",null=True, blank=True)
    created= models.IntegerField(verbose_name= "Año", null=True, blank=True)
    
    class Meta:
        verbose_name= "Proyecto"
        ordering= ["-order"]
    
    def __str__(self):
        return self.title 

class Study(models.Model):
    order = models.IntegerField(null=True, blank=True)
    title= models.CharField(max_length=200, verbose_name= "Titulo", null=True, blank=True)
    subtitle= models.CharField(max_length=200, verbose_name= "Subtitulo", null=True, blank=True)
    description= RichTextField(verbose_name= "Descripcion", null=True, blank=True)
    image= models.ImageField(verbose_name= "Imagen", upload_to="projects", null=True, blank=True)

    class Meta:
        verbose_name= "Estudio"
        ordering= ["-order"]
    
    def __str__(self):
        return self.title 

class Service(models.Model):
    order = models.IntegerField(null=True, blank=True)
    text= RichTextField(verbose_name= "Servicio", null=True, blank=True)

    class Meta:
        verbose_name= "Servicio"
        ordering= ["order"]

class Credit(models.Model):
    title= models.CharField(max_length=200, verbose_name= "Titulo", null=True, blank=True)
    link= models.URLField(verbose_name= "Link",null=True, blank=True)
    category= models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
    
    class Meta:
        verbose_name= "Crédito"

    def __str__(self):
        return self.title 
