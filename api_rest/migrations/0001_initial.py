# Generated by Django 4.2 on 2023-04-22 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('login', models.CharField(default='', max_length=30)),
                ('nome', models.CharField(default='', max_length=50)),
                ('senha', models.CharField(default='', max_length=30)),
            ],
        ),
    ]