from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone

# Manager custom pour user par email
class CuisinierManager(BaseUserManager):
    def create_user(self, email, nom, prenom, password=None):
        if not email:
            raise ValueError("Email obligatoire")
        email = self.normalize_email(email)
        user = self.model(email=email, nom=nom, prenom=prenom)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nom, prenom, password):
        user = self.create_user(email, nom, prenom, password)
        user.is_admin = True
        user.save(using=self._db)
        return user

class Cuisinier(AbstractBaseUser):
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = CuisinierManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nom', 'prenom']

    def __str__(self):
        return f"{self.prenom} {self.nom} ({self.email})"

    @property
    def is_staff(self):
        return self.is_admin

# Modèle recette
class Recette(models.Model):
    cuisinier = models.ForeignKey(Cuisinier, on_delete=models.CASCADE, related_name='recettes')
    titre = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos_recettes/', blank=True, null=True)
    ingredients = models.TextField(help_text="Liste des ingrédients")
    etapes = models.TextField(help_text="Étapes de la recette")
    date_creation = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titre
