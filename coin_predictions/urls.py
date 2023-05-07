from django.urls import path
from .views import CoinPredictionAPIView

urlpatterns = [
    path("<str:request_type>/", CoinPredictionAPIView.as_view(), name="get_coin_data"),
    path(
        "<str:request_type>/<str:coin_name>/",
        CoinPredictionAPIView.as_view(),
        name="get_coin_data",
    ),
]
