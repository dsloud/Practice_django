# Generated by Django 4.0 on 2022-01-12 05:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0002_remove_subject_post_id_post_subject'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='subject',
            new_name='subject_id',
        ),
    ]
