# Generated by Django 5.0 on 2023-12-24 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_users_teacher_delete_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='photo',
            field=models.FileField(blank=True, null=True, upload_to='photo/profile'),
        ),
    ]
