# Generated by Django 4.2 on 2024-04-23 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_testmodel_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testmodel',
            name='number',
            field=models.DecimalField(decimal_places=15, max_digits=16),
        ),
    ]
