from django.db import models
import uuid

from account.models import User
# Create your models here.

class CategoriaDespesa(models.Model):
    uuid = models.UUIDField(unique=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.name

class Despesa(models.Model):
    typeChoice = (
        ('1','Fixa'),
        ('2','Não Fixa'),
    )
    uuid = models.UUIDField(unique=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=255)
    value = models.FloatField()
    typeDespesa = models.CharField(
        max_length=1,
        choices = typeChoice
    )
    date = models.DateField()
    categoria = models.ForeignKey(CategoriaDespesa, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

