# Generated by Django 4.2.3 on 2023-09-01 16:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="url",
            name="pin",
            field=models.DecimalField(
                blank=True, decimal_places=0, max_digits=8, null=True
            ),
        ),
    ]