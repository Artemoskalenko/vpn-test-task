# Generated by Django 4.2.7 on 2023-11-14 00:11

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Site",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("site_name", models.CharField(max_length=255)),
                (
                    "original_url",
                    models.URLField(
                        max_length=255,
                        validators=[django.core.validators.URLValidator()],
                    ),
                ),
                ("sent_data", models.PositiveIntegerField(default=0)),
                ("downloaded_data", models.PositiveIntegerField(default=0)),
                ("number_of_transitions", models.PositiveIntegerField(default=0)),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "unique_together": {("original_url", "user_id")},
            },
        ),
    ]