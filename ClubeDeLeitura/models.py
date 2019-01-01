from django.db import models



class Colecao(models.Model):
	nome = models.CharField('nome da coleção',max_length=30)

	class Meta:
		verbose_name_plural='coleções'
		verbose_name='coleção'

	def __str__(self):
		return '{}'.format(self.nome)


		

class Revista(models.Model):
	numero_edicao = models.IntegerField('número de edição')
	ano = models.IntegerField()

	class Meta:
		verbose_name_plural = 'revistas'
		verbose_name = 'revista'
		ordering = ('-ano','numero_edicao')

	def __str__(self):
		return '{}'.format(self.numero_edicao)



class Caixa(models.Model):
	numero = models.IntegerField('número')
	etiqueta = models.CharField(max_length=40)
	cor = models.CharField(max_length=30)
	revista = models.ForeignKey(Revista, on_delete=models.CASCADE)

	class Meta:
		verbose_name_plural = 'caixas'
		verbose_name = 'caixa'
		ordering = ('-cor','numero')

	def __str__(self):
		return '{}'.format(self.numero)



class Amigo(models.Model):

	PREDIO = 'PREDIO'
	ESCOLA = 'ESCOLA'

	grupo_amigo_choices = (
        (PREDIO, 'Prédio'),
        (ESCOLA,'Escola'),
		)
	nome = models.CharField(max_length=40)
	nome_mae = models.CharField('nome da mãe',max_length=40)
	telefone = models.CharField(max_length=20)
	grupo_amigo = models.CharField('grupos de amigos',max_length=40,choices=grupo_amigo_choices)

	class Meta:
		verbose_name_plural = 'amigos'
		verbose_name = 'amigo'
		ordering = ('-nome_mae','nome')

	def __str__(self):
		return '{}'.format(self.nome)



class Emprestimo(models.Model):
	data_emprestimo = models.DateField('data de emprestimo')
	data_devolucao = models.DateField('data de devoluçao')
	revista = models.ForeignKey(Revista, on_delete=models.CASCADE)
	amigo = models.ForeignKey(Amigo, on_delete=models.CASCADE)

	class Meta:
		verbose_name_plural = 'emprestimos'
		verbose_name = 'emprestimo'
		ordering = ('-data_emprestimo','data_devolucao')

	def __str__(self):
		return '{} - {}'.format(self.revista,self.amigo)

    