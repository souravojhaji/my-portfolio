# Generated by Django 5.1.1 on 2024-09-25 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_remove_skill_proficiency_skill_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='about',
            old_name='description',
            new_name='content',
        ),
        migrations.AddField(
            model_name='about',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
