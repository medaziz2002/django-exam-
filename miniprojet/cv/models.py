from django.db import models

class Competance(models.Model) :
   competance_languistique = models.CharField(max_length=80)
   competance_technique = models.CharField(max_length=80)

class Formation(models.Model) :
    intitule=models.CharField(max_length=80)
    date=models.DateField()
    lieu=models.CharField(max_length=80)
    type = models.ForeignKey('Type',on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.intitule

class Stage(models.Model) :
    intitule=models.CharField(max_length=80)
    date=models.DateField()
    lieu=models.CharField(max_length=80)
    def __str__(self) -> str:
        return self.intitule

class Type(models.Model) :
    nomType=models.CharField(max_length=80)
    description=models.CharField(max_length=80)
    def __str__(self) -> str:
        return self.nomType



