# Generated by Django 4.1.5 on 2024-11-29 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appportfolio', '0011_alter_estado_estado_alter_estado_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estado',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='tarea',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]