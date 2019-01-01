from django.contrib import admin
from ClubeDeLeitura.models import Colecao,Revista,Caixa,Amigo,Emprestimo



admin.site.site_header='Local de Administração do Clube'
admin.site.site_title='Clubinho de Leitura'
admin.site.index_title='Clube'


class ColecaoAdmin(admin.ModelAdmin):
	list_display = ['nome']
	list_filter = ('nome',)
	search_fields = ('nome',)


class RevistaAdmin(admin.ModelAdmin):
	list_display = ('numero_edicao','ano')
	list_filter = ('ano',)

class CaixaAdmin(admin.ModelAdmin):
	list_display = ('numero','etiqueta','cor','revista')
	list_filter = ('numero','cor',)
	search_fields = ('cor',)

class AmigoAdmin(admin.ModelAdmin):
	list_display = ('nome','nome_mae','telefone','grupo_amigo')
	list_filter = ('nome','grupo_amigo',)
	search_fields = ('nome',)


class EmprestimoAdmin(admin.ModelAdmin):
	list_display = ('data_e','data_emprestimo','data_devolucao','revista','amigo')
	list_filter = ('data_emprestimo','data_devolucao',)
	date_hierarchy = 'data_emprestimo'

	def data_e(self,obj):
		return obj.data_emprestimo.strftime('%d/%m/%Y')
	data_e.short_description = 'data'
  



admin.site.register(Colecao,ColecaoAdmin)
admin.site.register(Revista,RevistaAdmin)
admin.site.register(Caixa,CaixaAdmin)
admin.site.register(Amigo,AmigoAdmin)
admin.site.register(Emprestimo,EmprestimoAdmin)


