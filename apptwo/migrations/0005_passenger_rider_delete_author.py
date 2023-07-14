# Generated by Django 4.2.2 on 2023-07-10 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apptwo', '0004_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Srn', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Rider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Srn', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='Author',
        ),
    ]