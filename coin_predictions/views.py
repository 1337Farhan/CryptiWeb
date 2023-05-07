from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import MethodNotAllowed
from .models import CoinPrediction

import json

# Create your views here.


class CoinPredictionAPIView(APIView):
    """
    Returns data about the coin predictions availabe in CryptiWeb.

    Endpoints:

        - /api/v1/get_request_types/  : returns all available request types.
        - /api/v1/get_coin_names/ : returns list of coins available on CryptiWeb.
        - /api/v1/get_coin_data/<coin_name>  : return a json object of a specific coin.
        - /api/v1/get_coin_predicted_prices/<coin_name>  : returns a serialized prediction list, provided the coin name.
        - /api/v1/get_all_coin_data/ : returns a list of coin_prediction objects.

    """

    allowed_methods = ["GET"]
    default_request_type = "get_request_types"
    allowed_request_types = [
        "get_coin_names",
        "get_coin_data",
        "get_coin_predicted_prices",
        "get_all_coin_data",
    ]

    def get(
        self, request, request_type=default_request_type, coin_name=None, format=None
    ):

        if request_type == self.default_request_type:
            return Response(self.allowed_request_types)

        elif request_type in self.allowed_request_types:
            if request_type == "get_coin_names":
                data = {
                    "coin_names": [
                        prediction.coin_name
                        for prediction in CoinPrediction.objects.all()
                    ]
                }
                return Response(data)

            elif request_type == "get_coin_data":
                coin_prediction = CoinPrediction.objects.get(coin_name=coin_name)
                data = {
                    "coin_name": coin_prediction.coin_name,
                    "predicted_prices": json.loads(coin_prediction.predicted_prices),
                    "prediction_date": coin_prediction.prediction_date.isoformat(),
                    "mse": coin_prediction.mse,
                    "rmse": coin_prediction.rmse,
                }
                return Response(data)

            elif request_type == "get_coin_predicted_prices":
                coin_prediction = CoinPrediction.objects.get(coin_name=coin_name)
                data = {
                    "predicted_prices": json.loads(coin_prediction.predicted_prices),
                    "prediction_date": coin_prediction.prediction_date.isoformat(),
                }
                return Response(data)

            elif request_type == "get_all_coin_data":
                coin_predictions = CoinPrediction.objects.all()
                data = []
                for coin_prediction in coin_predictions:
                    data.append(
                        {
                            "title": coin_prediction.coin_name,
                            "predicted_prices": json.loads(
                                coin_prediction.predicted_prices
                            ),
                            "prediction_date": coin_prediction.prediction_date.isoformat(),
                            "mse": coin_prediction.mse,
                            "rmse": coin_prediction.rmse,
                        }
                    )
                return Response(data)

            else:
                return Response("Request is not allowed.")

        else:
            return Response("Request type is not allowed.", status=403)
