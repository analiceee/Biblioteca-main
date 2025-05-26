from django.contrib import admin
from .models import Cidade, Autor, Editora, Leitor, Livro, Genero, Reserva

# Registrando todos os modelos uma única vez, como pede o estudo dirigido
admin.site.register(Cidade)
admin.site.register(Autor)
admin.site.register(Editora)
admin.site.register(Leitor)
admin.site.register(Livro)
admin.site.register(Genero)
admin.site.register(Reserva)
