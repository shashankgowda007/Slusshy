# Generated by Django 4.2.2 on 2023-07-04 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apptwo', '0002_signup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='password',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='signup',
            name='username',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
