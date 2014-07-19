# Create your views here.

from django.views.generic import ListView, DetailView
from genviewbks.models import Publisher

class PublisherList(ListView):
	model = Publisher
	template_name = 'genviewbks/publisher_list.html'
	context_object_name = 'all_publishers'

class PublisherDetail(DetailView):
	model = Publisher
	context_object_name = 'pub_detail'
	slug_field = 'name'
