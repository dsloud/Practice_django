# Generated by Django 4.0.1 on 2022-01-11 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_usermodel_connection'),
        ('community', '0003_communitymodel_admin_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='communitymodel',
            name='community_admin_id',
            field=models.ForeignKey(db_column='community_admin_id', on_delete=django.db.models.deletion.CASCADE, related_name='community_admin', to='user.usermodel'),
        ),
    ]
