# Generated by Django 2.1.5 on 2019-02-17 18:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='tile',
            new_name='title',
        ),
    ]
