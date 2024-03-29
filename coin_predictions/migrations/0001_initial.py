# Generated by Django 4.2 on 2023-04-21 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CoinPrediction",
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
                ("coin_name", models.CharField(max_length=255)),
                ("predicted_prices", models.CharField(max_length=255)),
                ("prediction_date", models.DateTimeField()),
                ("mse", models.FloatField(default=0)),
                ("rmse", models.FloatField(default=0)),
                ("last_updated", models.DateTimeField(auto_now=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "verbose_name": "Coin Prediction",
                "verbose_name_plural": "Coin Predictions",
                "ordering": ["-last_updated"],
            },
        ),
    ]
