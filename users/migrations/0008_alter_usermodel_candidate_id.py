# Generated by Django 4.0.1 on 2022-03-08 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_usermodel_if_face_verified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='candidate_id',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
