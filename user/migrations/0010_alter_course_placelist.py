# Generated by Django 5.0.7 on 2024-07-27 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_alter_course_placelist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='placelist',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
