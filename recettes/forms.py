from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Cuisinier, Recette

class InscriptionForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Cuisinier
        fields = ['nom', 'prenom', 'email', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

class ConnexionForm(AuthenticationForm):
    username = forms.EmailField(label="Email")

    class Meta:
        model = Cuisinier
        fields = ['username', 'password']

class RecetteForm(forms.ModelForm):
    class Meta:
        model = Recette
        fields = ['titre', 'description', 'photo', 'ingredients', 'etapes']
