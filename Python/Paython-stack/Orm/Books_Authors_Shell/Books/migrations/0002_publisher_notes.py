# Generated by Django 2.2.4 on 2022-10-03 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='publisher',
            name='notes',
            field=models.CharField(default='ok', max_length=255),
            preserve_default=False,
        ),
    ]