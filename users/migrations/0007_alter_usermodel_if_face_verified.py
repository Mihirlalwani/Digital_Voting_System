# Generated by Django 4.0.1 on 2022-03-08 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_usermodel_candidate_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='if_face_verified',
            field=models.BooleanField(default=False),
        ),
    ]
