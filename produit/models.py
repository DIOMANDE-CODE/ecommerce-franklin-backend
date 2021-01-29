from django.db import models

# Create your models here.

class Image(models.Model):
    image=models.ImageField(verbose_name="background")

    def __str__(self):
        return self.image

class Categorie(models.Model):
    categorie=models.CharField(max_length=255, blank=False)
    image=models.ImageField(null=True)

    class Meta:
        ordering=['categorie']

    def __str__(self):
        return self.categorie

class Fruit(models.Model):
    nom_fruit=models.CharField(max_length=255, verbose_name="Nom de l'article", blank=False)
    information_fruit=models.TextField(verbose_name="detail du l'article", blank=False)
    prix_fruit=models.IntegerField( verbose_name="Prix de l'article",blank=False)
    quantite=models.IntegerField( verbose_name="Nombre d'article disponible",blank=False,default=1)
    poids=models.IntegerField( verbose_name="Poids de l'article",blank=False)
    categorie=models.ForeignKey(Categorie,on_delete=models.CASCADE, verbose_name="Categorie de l'article", related_name='fruits')
    nom_categorie=models.CharField(max_length=255,null=True)
    prix=models.IntegerField(verbose_name="prix total",null=True)
    Image=models.ImageField(verbose_name="Image de l'article")

    def save(self,*args,**kwargs):
        self.nom_categorie=self.categorie.categorie
        super(Fruit,self).save(*args,**kwargs)


    def __str__(self):
        return "{} , {} , {} , {} , {} ".format(self.nom_fruit, self.information_fruit, self.prix_fruit, self.quantite, self.poids)