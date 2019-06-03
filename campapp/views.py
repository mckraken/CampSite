from django.views.generic import TemplateView

# Create your views here.

class HomeView(TemplateView):
    template_name = "homepage.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["test"] = 5
        return context