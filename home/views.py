from django.shortcuts import render
from django.views.generic.base import TemplateView


# Create your views here.
# Create your views here.
class Home(TemplateView):
	template_name = 'home/home.html'	
	
	def get_context_data(self, *args, **kwargs):
		context = super(Home, self).get_context_data(*args, **kwargs)
		return context