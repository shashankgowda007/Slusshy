# Generated by Django 4.2.2 on 2023-07-10 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apptwo', '0008_alter_mapval_mapp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mapval',
            name='Mapp',
            field=models.JSONField(),
        ),
    ]