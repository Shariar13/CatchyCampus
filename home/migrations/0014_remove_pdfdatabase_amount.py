# Generated by Django 4.2.1 on 2023-06-03 18:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_pdfdatabase_amount_pdfdatabase_total_cost_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pdfdatabase',
            name='amount',
        ),
    ]
