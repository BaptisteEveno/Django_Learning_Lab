from django.db import models


class Framework(models.Model):
    nom = models.CharField(max_length=100)
    categorie = models.CharField(max_length=100)
    date_creation = models.DateField()
    derniere_version = models.CharField(max_length=50)
    site_web = models.URLField()

    def __str__(self):
        return self.nom
