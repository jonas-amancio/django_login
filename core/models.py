from django.db import models
# from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.conf import settings

    

class UsuarioManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **kwargs):
        if not email:
            raise ValueError('O e-mail é obrigatório')
        email = self.normalize_email(email)
        user = self.model(email=email, username=email, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user
    

    def create_user(self, email, password=None, **kwargs):
        kwargs.setdefault('is_superuser', False)
        return self._create_user(email, password, **kwargs)
    

    def create_superuser(self, email, password, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)

        if(kwargs.get('is_superuser') is not True):
            raise ValueError('Superuser precisa ter is_superuser=True')
        
        if(kwargs.get('is_staff') is not True):
            raise ValueError('Superuser precisa ter is_staff=True')
        
        return self._create_user(email, password, **kwargs)


class CustomUsuario(AbstractUser):
    email = models.EmailField('E-mail', unique=True)
    telefone = models.CharField('Telefone', max_length=15)
    is_staff = models.BooleanField('Membro da equipe', default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'telefone']

    def __str__(self):
        return self.email
    
    objects = UsuarioManager()




class Post(models.Model):
    # FK para a model de usuário padrão do django
    # autor = models.ForeignKey(get_user_model(), verbose_name='Autor', on_delete=models.CASCADE)
    autor = models.ForeignKey(CustomUsuario, verbose_name='Autor', on_delete=models.CASCADE)
    titulo = models.CharField('Título', max_length=100)
    texto = models.TextField('Texto', max_length=400)

    def __str__(self):
        return self.titulo