# Generated by Django 4.0 on 2022-01-06 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('login_id', models.CharField(max_length=30)),
                ('login_pw', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=30)),
                ('nickname', models.CharField(max_length=30)),
            ],
        ),
    ]
