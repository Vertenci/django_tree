from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import MenuItem


class MenuItemDetailView(DetailView):
    model = MenuItem
    template_name = 'page_for_item.html'

    def get_object(self, queryset=None):
        title = self.kwargs.get('title')
        return get_object_or_404(MenuItem, title=title)


def some_page(request):
    return render(request, 'mn/page.html')
