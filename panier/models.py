from django.db import models
# Create your models here.

class Chariot(models.Model):
    image=models.ImageField(verbose_name="Image de l'article",null=True)
    nom_article_commande=models.CharField(verbose_name="nom de l'article",blank=False,max_length=255,null=True)
    prix_article=models.IntegerField(verbose_name="prix de l'article", blank=False, null=True)
    quantite=models.IntegerField(verbose_name="quantite commandé", blank=False,default=0,null=True)
    total=models.IntegerField(verbose_name="Prix total de l'article commandé", blank=False,default=0,null=True)
    date=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['date']

    def __str__(self):
        return self.nom_article_commande