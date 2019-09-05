from django.shortcuts import render
from django.views import generic
from .forms import NewsForm
from django.contrib.messages.views import SuccessMessageMixin
from .models import News,Notification


# Create your views here.
class Test(generic.TemplateView):
    template_name = "main.html"

    def get_context_data(self, **kwargs):
        context = {}
        context['post'] = News.objects.all()
        context['notification']=Notification.objects.all()
        return context


class CreateNews(SuccessMessageMixin, generic.CreateView):
    template_name = "index.html"
    form_class = NewsForm
    success_url = '/'
    success_message = 'xeber sayta elave olundu'

    def form_valid(self, form):
        news = form.save()

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = {}
        context['form'] = NewsForm()
        return context

class NewsDetail(generic.DeleteView):
    model = News
    template_name ="detail.html"