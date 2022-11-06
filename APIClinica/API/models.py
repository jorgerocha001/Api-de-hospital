from django.db import models

# Create your models here.
class Medico(models.Model):
    nome = models.CharField(
        max_length=255,
        null= False,
        blank= False
        )
    
    sobrenome = models.CharField(
        max_length= 255,
        null= False,
        blank= False
    )

    crm = models.CharField(
        max_length=20,
        null= False,
        blank= False
    )

    especializacao = models.CharField(
        max_length=255,
        null= False,
        blank= False
    )

    senhaMedico = models.CharField(
        max_length=255,
        null= True,
        blank= False,
        default= None
    )


class Consultas(models.Model):
    nome_paciente = models.CharField(
        max_length=255,
        null= False,
        blank= False,
    )

    medico = models.ForeignKey(
        to = Medico,
        on_delete = models.CASCADE,
        related_name= "consulta",
        null= False,
        blank= False
    )