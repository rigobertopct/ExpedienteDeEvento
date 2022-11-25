# Generated by Django 3.2.6 on 2022-11-25 20:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Atleta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250, verbose_name='Nombre')),
                ('apel', models.CharField(max_length=250, verbose_name='Apellido')),
                ('fecha', models.DateField(verbose_name='Fecha de Nacimiento')),
            ],
            options={
                'verbose_name': 'atletas',
                'verbose_name_plural': 'atletas',
                'db_table': 'atletas',
            },
        ),
        migrations.CreateModel(
            name='CodEvento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250, verbose_name='Nombre de la disciplina')),
                ('descripcion', models.CharField(max_length=1000, verbose_name='Descripción')),
            ],
            options={
                'verbose_name': 'codEvento',
                'verbose_name_plural': 'codEventos',
                'db_table': 'codEventos',
            },
        ),
        migrations.CreateModel(
            name='Deporte',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250, verbose_name='Nombre del deporte')),
            ],
            options={
                'verbose_name': 'Deporte',
                'verbose_name_plural': 'Deportes',
                'db_table': 'deportes',
            },
        ),
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250, verbose_name='Nombre de la disciplina')),
                ('deporte_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.deporte')),
            ],
            options={
                'verbose_name': 'disciplina',
                'verbose_name_plural': 'disciplinas',
                'db_table': 'disciplinas',
            },
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250, verbose_name='Nombre de la disciplina')),
                ('sigla', models.CharField(max_length=250, verbose_name='Siglas')),
            ],
            options={
                'verbose_name': 'pais',
                'verbose_name_plural': 'paises',
                'db_table': 'paises',
            },
        ),
        migrations.CreateModel(
            name='Participacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('atleta_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.atleta')),
                ('disciplina_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.disciplina')),
                ('evento_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.codevento')),
            ],
            options={
                'verbose_name': 'participacion',
                'verbose_name_plural': 'participacions',
                'db_table': 'participacions',
            },
        ),
    ]
