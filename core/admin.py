from typing import Any
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Post, CustomUsuario
from .forms import CustomUsuarioCreateForm, CustomUsuarioChangeForm

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', '_autor')
    exclude = ['autor']

    def _autor(self, instance):
        return f'{instance.autor.get_full_name()}'
    

    def get_queryset(self, request):
        qs = super(PostAdmin, self).get_queryset(request)
        return qs.filter(autor=request.user)
    

    def save_model(self, request, obj, form, change):
        obj.autor = request.user
        return super().save_model(request, obj, form, change)


@admin.register(CustomUsuario)
class CustomUsuarioAdmin(UserAdmin):
    add_form = CustomUsuarioCreateForm
    form = CustomUsuarioChangeForm
    model = CustomUsuario
    list_display = ('first_name', 'last_name', 'email', 'telefone', 'is_staff')
    fieldsets = (
        (None, {
            'fields': (
                'email',
                'password',
            ),
        }),
        ('Informações Pessoais', {
            'fields': (
                'first_name',
                'last_name',
                'telefone',
            ),
        }),
        ('Permissões', {
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser', 
                'groups',
                'user_permissions',
            ),
        }),
        ('Datas Importantes', {
            'fields': (
                'last_login',
                'date_joined',
            )
        })
    )
    