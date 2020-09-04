# Generated by Django 3.0 on 2020-09-04 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consultorio',
            fields=[
                ('cuit', models.IntegerField(primary_key=True, serialize=False)),
                ('nombresDelConsultorio', models.CharField(max_length=10)),
                ('domicilio', models.TextField()),
                ('mail', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('dni', models.IntegerField(primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=10)),
                ('apellido', models.CharField(max_length=10)),
                ('domicilio', models.TextField()),
                ('mail', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=15)),
            ],
        ),
    ]
