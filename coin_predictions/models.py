from django.db import models
import json

# Create your models here.


class CoinPrediction(models.Model):
    coin_name = models.CharField(max_length=255, blank=False, null=False)
    predicted_prices = models.CharField(max_length=255, blank=False, null=False)
    prediction_date = models.DateTimeField(blank=True, null=True)
    mse = models.FloatField(default=0)
    rmse = models.FloatField(default=0)
    last_updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-last_updated"]
        verbose_name = "Coin Prediction"
        verbose_name_plural = "Coin Predictions"

        def __str__(self):
            return f"""{self.coin_name} + prediction instance updated on {self.last_updated}, 
                        prediction performed on {self.prediction_date}"""

    def set_predicted_prices(self, predicted_prices):
        self.predicted_prices = json.dumps(predicted_prices)

    def get_predicted_prices(self):
        return json.loads(self.predicted_prices)
