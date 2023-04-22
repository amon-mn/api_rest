from django.db import models
import uuid


class Usuario(models.Model):
    
    id = models.UUIDField(default=uuid.uuid4, editable=False)
    login = models.CharField(primary_key=True, max_length=30, default='')
    nome = models.CharField(max_length=50, default='')
    senha = models.CharField(max_length=30, default='')

    def __str__(self):
        return f'Nome: {self.nome} | Login: {self.login} | Senha: {self.senha}'