# Generated by Django 4.0 on 2022-01-07 08:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0002_usermodel_connection_usermodel_sex_selection'),
        ('community', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blacklist',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('blocked_id', models.ForeignKey(db_column='blocked_id', on_delete=django.db.models.deletion.CASCADE, related_name='blk_id', to='user.usermodel')),
                ('comm_id', models.ForeignKey(db_column='comm_id', on_delete=django.db.models.deletion.CASCADE, related_name='com_id', to='community.communitymodel')),
            ],
        ),
    ]
