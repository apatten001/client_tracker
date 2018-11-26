from django.shortcuts import render
from django.views.generic import DetailView
from .models import Client
from measurement.models import Measurement
# Create your views here.


def client_list_view(request):
    clients = Client.objects.all()
    return render(request, 'client/index.html', {'clients': clients})


class ClientProfileView(DetailView):
    # page_content = 'returns a profile of a specific client'
    template_name = 'client/profile.html'
    queryset = Measurement.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ClientProfileView, self).get_context_data(**kwargs)
        context['client'] = Client.objects.all()
        return context




