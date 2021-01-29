from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class ClientManager(BaseUserManager):
    def create_user(self,email,nom,prenom,numero,password=None):
        user=self.model(
            email=self.normalize_email(email),
            nom=nom,
            prenom=prenom,
            numero=numero
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,nom,prenom,numero,password=None):
        user=self.create_user(
            email=email,
            nom=nom,
            prenom=prenom,
            numero=numero,
            password=password
        )
        user.is_admin=True
        user.is_superuser=True
        user.is_staff=True
        user.save(using=self._db)
        return user

class Client(AbstractBaseUser):
    email=models.EmailField(verbose_name="Adresse Email",max_length=60,unique=True)
    nom=models.CharField(verbose_name="Nom",max_length=255,null=True)
    prenom=models.CharField(verbose_name="prenom",max_length=255,null=True)
    numero=models.CharField(verbose_name="numero",max_length=255,null=True)
    is_admin=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)

    USERNAME_FIELD="email"

    REQUIRED_FIELDS=['nom','prenom','numero']

    objects=ClientManager()

    def __str__(self):
        return self.nom

    def has_perm(self,perm,obj=None):
        return True

    def has_module_perms(self,app_label):
        return True

