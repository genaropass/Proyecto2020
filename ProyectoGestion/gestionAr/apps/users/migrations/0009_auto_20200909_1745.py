# Generated by Django 3.0 on 2020-09-09 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20200909_1733'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Paciente',
        ),
        migrations.AddField(
            model_name='listaturnosmedico1',
            name='medicos',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='listaturnosmedico2',
            name='medicos',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
