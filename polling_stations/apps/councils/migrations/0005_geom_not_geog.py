# Generated by Django 2.2.10 on 2020-02-14 14:41

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("councils", "0004_auto_20200203_1040"),
    ]

    operations = [
        migrations.AlterField(
            model_name="council",
            name="area",
            field=django.contrib.gis.db.models.fields.MultiPolygonField(
                blank=True, null=True, srid=4326
            ),
        ),
    ]
