from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = "index.html"

class ClientView(TemplateView):
    template_name = "client.html"

class ProductionAreaView(TemplateView):
    template_name = "production_area.html"