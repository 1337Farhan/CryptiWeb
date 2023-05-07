from django.views.generic import ListView, DetailView

from coin_predictions.models import CoinPrediction


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

    def get_queryset(self):
        return CoinPrediction.objects.filter(pk=self.kwargs["pk"])
