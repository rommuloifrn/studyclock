# Generated by Django 4.0 on 2023-08-14 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_session_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='notes',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
