# Generated by Django 4.2 on 2023-04-22 05:22

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api_rest', '0002_alter_user_login'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('login', models.CharField(default='', max_length=30, primary_key=True, serialize=False)),
                ('nome', models.CharField(default='', max_length=50)),
                ('senha', models.CharField(default='', max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]