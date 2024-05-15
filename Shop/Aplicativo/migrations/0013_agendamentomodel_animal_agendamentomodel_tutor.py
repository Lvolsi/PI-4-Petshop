# Generated by Django 5.0.4 on 2024-05-15 18:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aplicativo', '0012_alter_agendamentomodel_adestramento_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='agendamentomodel',
            name='animal',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Aplicativo.cadastroanimalmodel'),
        ),
        migrations.AddField(
            model_name='agendamentomodel',
            name='tutor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
