# Generated by Django 4.2.2 on 2023-07-13 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apptwo', '0013_rate_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='rate',
            name='bestrider',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
