from django.shortcuts import render
from django.views import generic, View
from .models import Stock, Price
from .forms import SearchForm


class Search(View):
    def get(self, request):
        form = SearchForm()

        return render(request, 'market/search.html', {
            "form": form
        })


class StockListView(generic.ListView):
    model = Stock
    template_name = 'market/stock_list.html'
    context_object_name = 'stock_list'
    paginate_by = 5

    def get_queryset(self):
        return Stock.objects.all().order_by('ticker')


class StockDetailView(generic.DetailView):
    # slug is ticker in this case
    model = Stock
    template_name = 'market/stock_detail.html'
    context_object_name = 'stock'

    def get_context_data(self, **kwargs):
        context = super(StockDetailView, self).get_context_data(**kwargs)
        context['price_list'] = Price.objects.filter(
            stock=self.object).order_by('-date')
        return context

    def get_object(self):
        ticker = self.kwargs.get("slug")
        return Stock.objects.get(ticker=ticker)
