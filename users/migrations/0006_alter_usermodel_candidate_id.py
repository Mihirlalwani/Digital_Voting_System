# Generated by Django 4.0.1 on 2022-03-08 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_candidte_candidate_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='candidate_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
