# Generated by Django 2.1.4 on 2018-12-28 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Amigo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=40)),
                ('nome_mae', models.CharField(max_length=40, verbose_name='nome da mãe')),
                ('telefone', models.CharField(max_length=20)),
                ('grupo_amigo', models.CharField(choices=[('PREDIO', 'Prédio'), ('ESCOLA', 'Escola')], max_length=40, verbose_name='grupos de amigos')),
            ],
        ),
        migrations.CreateModel(
            name='Caixa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField(verbose_name='número')),
                ('etiqueta', models.CharField(max_length=40)),
                ('cor', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Colecao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30, verbose_name='nome da coleção')),
            ],
        ),
        migrations.CreateModel(
            name='Emprestimo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_emprestimo', models.DateField(verbose_name='data de emprestimo')),
                ('data_devolucao', models.DateField(verbose_name='data de devoluçao')),
                ('amigo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ClubeDeLeitura.Amigo')),
            ],
        ),
        migrations.CreateModel(
            name='Revista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_edicao', models.IntegerField(verbose_name='número de edição')),
                ('ano', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='emprestimo',
            name='revista',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ClubeDeLeitura.Revista'),
        ),
        migrations.AddField(
            model_name='caixa',
            name='revista',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ClubeDeLeitura.Revista'),
        ),
    ]
