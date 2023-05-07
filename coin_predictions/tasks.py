import boto3
from CryptiWeb import settings
import json
from .models import CoinPrediction
from datetime import datetime

def update_coins():
    s3 = boto3.resource(
        service_name='s3',
        region_name=settings.AWS_DEFAULT_REGION,
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
    )

    bucket = s3.Bucket("crypti-predict").objects.all()

    coins_data = list()
    
    for object in bucket:
        coins_data.append(json.loads(object.get()["Body"].read().decode()))

    for coin_data in coins_data:
        coin, _ = CoinPrediction.objects.get_or_create(
            coin_name = coin_data["coin_name"],
        )

        coin.mse = float(coin_data["mse"])
        coin.rmse = float(coin_data["rmse"])
        coin.set_predicted_prices(coin_data["prediction_price_list"])
        coin.prediction_date = datetime.fromisoformat(coin_data["timestamp"])
        coin.save()