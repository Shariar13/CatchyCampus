# Generated by Django 4.1.3 on 2023-05-03 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_shoplist_shopphoto'),
    ]

    operations = [
        migrations.CreateModel(
            name='PDFDatabase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sendername', models.CharField(blank=True, max_length=99, null=True)),
                ('senderemail', models.CharField(blank=True, max_length=99, null=True)),
                ('senderphone', models.CharField(blank=True, max_length=99, null=True)),
                ('selectedshopusername', models.CharField(blank=True, max_length=99, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='file/')),
            ],
        ),
    ]
