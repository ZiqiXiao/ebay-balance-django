# Generated by Django 4.2.5 on 2023-10-05 13:07

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CheckingHistory",
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
                ("gift_card_no", models.CharField(max_length=13)),
                ("balance", models.CharField(max_length=10)),
                ("time", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
