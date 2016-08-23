from django.db import models
class Equipo(models.Model):
    nombre_equipo = models.CharField(max_length=60)
    f_creacion = models.DateField()
    Direccion = models.TextField()
    def __unicode__(self):
        return u'%s' % (
            self.nombre_equipo,
            )
class Poder(models.Model):
   nombre_poder = models.CharField(max_length=32)
   descripcion = models.CharField(max_length=500)
   def __unicode__(self):
        return u'%s' % (
            self.nombre_poder,
            )
GRUPO_SANGUINEO = ( ('O', 'O (Universal)'),
                    ('A', 'Grupo A'),
                    ('B', 'Grupo B'),
                    ('AB', 'Grupo AB') )
class Heroe(models.Model):
    nombre_heroe = models.CharField(max_length=120)
    identidad = models.CharField(max_length=170)
    f_nacimiento = models.DateField()
    nivel = models.IntegerField()
    grupo_sanguineo = models.CharField(
        max_length=2,
        choices=GRUPO_SANGUINEO,
        )
    foto = models.FileField(upload_to='fotos')
    correo = models.EmailField()
    equipo = models.ForeignKey(Equipo, blank=True)
    poderes = models.ManyToManyField(Poder)
    
    def __unicode__(self):
        return u'%s (Nivel %d)' % (
            self.nombre_heroe,
            self.nivel,
            )
    def lista_poderes(self):
        return ', '.join([x.nombre_poder for x in self.poderes.all()])

class Avistamiento(models.Model):
    f_avistamiento = models.DateTimeField()
    latitud = models.FloatField()
    longitud = models.FloatField()
    heroe = models.ForeignKey(Heroe)
    def __unicode__(self):
        return u'%s' % (
            self.heroe,
            )


