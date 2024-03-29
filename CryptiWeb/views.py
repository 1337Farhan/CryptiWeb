import datetime
from typing import Any, Dict
from django.views.generic import ListView, DetailView, TemplateView

from coin_predictions.models import CoinPrediction
from pycoingecko import CoinGeckoAPI
from calendar import monthrange
import numpy as np
import math

class MainView(ListView):
    template_name = "CryptiWeb/main.html"
    model = CoinPrediction
    context_object_name = "coins"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CoinView(DetailView):
    template_name = "CryptiWeb/coin_page.html"
    model = CoinPrediction
    cg = CoinGeckoAPI()

    def get_queryset(self):
        return self.model.objects.filter(pk=self.kwargs["pk"])
    
    def get_real_prices(self):
        coin = self.model.objects.get(pk=self.kwargs["pk"])
        prediction_day = coin.prediction_date.day
        today = datetime.datetime.now().day
        day_range = abs(today - prediction_day)
        
        data = self.cg.get_coin_market_chart_by_id(id=coin.coin_name, vs_currency="usd", days=day_range, interval="daily")

        real_prices = list()

        for price_data in data["prices"]:
            real_prices.append(price_data[1])

        return real_prices

    def get_days(self):
        coin = self.model.objects.get(pk=self.kwargs["pk"])
        num_days = monthrange(coin.prediction_date.year, coin.prediction_date.month)[1]

        days = list()

        for i in range(num_days):
            date = coin.prediction_date + datetime.timedelta(days=i)
            days.append(date)

        return days

    def get_coin_data(self, coin_id):
        coin_data = self.cg.get_coin_by_id(
            id=coin_id, localization=False, 
            tickers=True, market_data=True,
            community_data=False, developer_data=False,
            sparkline=False    
        )
    
        data = {
            "coin_image_link": coin_data.get("image").get("small"),
            "change_24h": coin_data.get("market_data").get("price_change_percentage_24h"), # Percentage
            "change_30d": coin_data.get("market_data").get("price_change_percentage_30d"), # Percentage
            "market_cap": coin_data.get("market_data").get("market_cap").get("usd")
        }
        
        try: data["coin_github_link"] =  coin_data.get("links").get("repos_url").get("github")[0] 
        except: data["coin_github_link"] = "#"

        try: data["coin_page"] =  coin_data.get("links").get("homepage")[0]
        except: data["coin_page"] = "#"

        try: data["coin_desc"] =  coin_data.get("description").get("en")
        except: data["coin_desc"] = ""

        return data

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        coin = context["object"]
        coin_data = self.get_coin_data(coin_id=coin.coin_name)
        today = datetime.datetime.now().day
        prediction_days = self.get_days()
        real_prices = self.get_real_prices()
        context["coin_data"] = coin_data
        context["real_prices"] = real_prices
        context["days"] = prediction_days
        context["rmse"] = math.sqrt(np.square(np.subtract(real_prices, coin.get_predicted_prices()[:len(real_prices)])).mean())
        context["todays_predicted_price"] = coin.get_predicted_prices()[today]
        context["current_real_price"] = real_prices[-1]

        return context
    
class AboutView(TemplateView):
    template_name = "CryptiWeb/about.html"
