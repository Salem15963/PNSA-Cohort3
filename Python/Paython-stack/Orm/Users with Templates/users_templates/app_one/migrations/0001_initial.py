# Generated by Django 2.2.4 on 2022-09-27 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('last', models.CharField(max_length=45)),
                ('email', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
            ],
        ),
    ]