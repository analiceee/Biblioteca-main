from django.contrib import admin
from .models import Cidade, Autor, Editora, Leitor, Genero, Livro

class LivroInlineAutor(admin.TabularInline):
    model = Livro
    extra = 1

class LivroInlineEditora(admin.TabularInline):
    model = Livro
    extra = 1

class LivroInlineGenero(admin.TabularInline):
    model = Livro
    extra = 1

class AutorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cidade')
    search_fields = ('nome',)
    inlines = [LivroInlineAutor]

class EditoraAdmin(admin.ModelAdmin):
    list_display = ('nome', 'site', 'cidade')
    search_fields = ('nome',)
    inlines = [LivroInlineEditora]

class GeneroAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    inlines = [LivroInlineGenero]

class LivroAdmin(admin.ModelAdmin):
    list_display = ('nome', 'autor', 'editora', 'genero', 'preco', 'data_pub', 'status')
    search_fields = ('nome', 'autor__nome', 'editora__nome', 'genero__nome')
    list_filter = ('status', 'genero')

admin.site.register(Autor, AutorAdmin)
admin.site.register(Editora, EditoraAdmin)
admin.site.register(Genero, GeneroAdmin)
admin.site.register(Livro, LivroAdmin)
admin.site.register(Cidade)
admin.site.register(Leitor)
