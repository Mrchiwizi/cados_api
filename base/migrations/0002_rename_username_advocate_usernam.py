# Generated by Django 4.1.5 on 2023-01-23 09:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='advocate',
            old_name='username',
            new_name='usernam',
        ),
    ]