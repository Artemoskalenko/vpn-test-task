import requests

from bs4 import BeautifulSoup

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, Http404
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView

from .services import link_replacement_function, serialize
from .models import Site


class SitesPage(LoginRequiredMixin, ListView):
    model = Site
    template_name = 'vpn/sites.html'
    context_object_name = 'sites'
    login_url = '/login/'

    def get_queryset(self):
        return Site.objects.filter(user_id=self.request.user.id)

    def post(self, request, *args, **kwargs):
        site_name = request.POST['site_name']
        original_url = request.POST['original_url']
        Site.objects.create(site_name=site_name, original_url=original_url, user_id=request.user)
        return redirect('sites')


class SiteDelete(LoginRequiredMixin, DeleteView):
    model = Site
    success_url = reverse_lazy('sites')


class StatisticsPage(LoginRequiredMixin, ListView):
    model = Site
    template_name = 'vpn/statistics.html'
    context_object_name = 'sites'
    login_url = '/login/'

    def get_queryset(self):
        return Site.objects.filter(user_id=self.request.user.id)


@login_required
def vpn_page(request, site_name, site_path=""):
    """displaying a page via VPN"""
    try:
        site = Site.objects.get(user_id=request.user, site_name=site_name)
    except Site.DoesNotExist:
        raise Http404("No Site matches the given query")

    # Parsing the page, changing links within the page and getting the final response
    url = site.original_url + site_path
    site_name = site.site_name
    page = requests.get(url, stream=True)
    soup = BeautifulSoup(page.content, "html.parser")
    transformed_page = link_replacement_function(url=site.original_url.rstrip('/'), soup=soup, site_name=site_name)
    response = HttpResponse(str(transformed_page), status=page.status_code)

    # Counting the number of bytes sent and received
    request_weight_in_bytes = len(serialize(request))
    response_weight_in_bytes = len(response.__bytes__())
    site.sent_data += request_weight_in_bytes
    site.received_data += response_weight_in_bytes
    site.number_of_transitions += 1
    site.save()
    return response

