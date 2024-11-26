# Generated by Django 5.1.3 on 2024-11-21 20:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("LLM_interaction", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="IndexNameStatus",
            fields=[
                (
                    "index_name",
                    models.UUIDField(editable=False, primary_key=True, serialize=False),
                ),
                (
                    "status",
                    models.IntegerField(
                        choices=[
                            (0, "Received"),
                            (1, "Error Occurred"),
                            (2, "In Progress"),
                            (3, "Ready"),
                        ],
                        default=0,
                    ),
                ),
            ],
        ),
        migrations.AlterField(
            model_name="userusagehistory",
            name="index_name",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="LLM_interaction.indexnamestatus",
            ),
        ),
    ]