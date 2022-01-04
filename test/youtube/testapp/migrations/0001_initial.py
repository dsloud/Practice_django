# Generated by Django 4.0 on 2022-01-04 01:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('select_sex', '0001_initial'),
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
                ('sex_selection', models.ForeignKey(db_column='sex_selection', on_delete=django.db.models.deletion.CASCADE, related_name='sex', to='select_sex.selectsexmodel')),
            ],
        ),
    ]