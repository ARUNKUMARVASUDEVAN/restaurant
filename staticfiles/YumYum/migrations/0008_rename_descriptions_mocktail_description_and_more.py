# Generated by Django 5.0.6 on 2024-08-18 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('YumYum', '0007_rename_mocktails_mocktail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mocktail',
            old_name='descriptions',
            new_name='description',
        ),
        migrations.AlterField(
            model_name='mocktail',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
