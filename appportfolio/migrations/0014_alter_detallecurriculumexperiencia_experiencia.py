# Generated by Django 4.1.5 on 2024-12-02 12:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appportfolio', '0013_alter_detallecurriculumexperiencia_experiencia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detallecurriculumexperiencia',
            name='experiencia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appportfolio.estudio'),
        ),
    ]
