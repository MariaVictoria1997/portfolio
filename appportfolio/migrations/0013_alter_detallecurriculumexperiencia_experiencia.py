# Generated by Django 4.1.5 on 2024-12-02 12:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appportfolio', '0012_alter_estado_id_alter_tarea_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detallecurriculumexperiencia',
            name='experiencia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appportfolio.experiencia'),
        ),
    ]
