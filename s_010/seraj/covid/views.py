from django.views.generic import TemplateView
from .api_covid19 import covid_analytics
from .api_chatgpt import chat

class CovidView(TemplateView):
    template_name = "covid/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["new_deaths"], context["total_deaths"] = covid_analytics()
        context["covid"] = chat()
        return context
    
