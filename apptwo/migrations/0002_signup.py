# Generated by Django 4.2.2 on 2023-07-04 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apptwo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
