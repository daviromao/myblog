from django.views.generic import TemplateView


class AboutPageView(TemplateView):
    template_name = 'about.html'

class WorkPageView(TemplateView):
    template_name = 'works.html'
    