# Generated by Django 3.2 on 2021-04-10 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commands', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='gender',
            field=models.CharField(choices=[('U', 'Undefined'), ('M', 'Male'), ('F', 'Female')], default='U', max_length=6),
        ),
    ]
