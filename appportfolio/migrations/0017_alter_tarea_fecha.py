# Generated by Django 4.1.5 on 2024-12-03 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appportfolio', '0016_alter_curriculum_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarea',
            name='fecha',
            field=models.DateTimeField(),
        ),
    ]
