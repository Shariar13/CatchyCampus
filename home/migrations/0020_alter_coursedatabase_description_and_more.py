# Generated by Django 4.2.1 on 2023-07-27 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_coursedatabase'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursedatabase',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='coursedatabase',
            name='syllabus',
            field=models.TextField(blank=True, null=True),
        ),
    ]
