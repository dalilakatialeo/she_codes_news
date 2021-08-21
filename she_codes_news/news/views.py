from django.views import generic
from .models import NewsStory
from .forms import StoryForm
from django.urls import reverse_lazy


class IndexView(generic.ListView):
    template_name = 'news/index.html'

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.order_by("pub_date")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.all()[:4]
        context['all_stories'] = NewsStory.objects.all()
        return context

class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'

class AddStoryView(generic.CreateView):
    form_class = StoryForm
    context_object_name = 'storyForm'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index') #we use the name we called the path in urlpatterns to get the url path

    def form_valid(self, form): #set author to user logged in
        form.instance.author = self.request.user
        return super().form_valid(form) #overriding form_valid which is a generic.createView

# class UpdateStoryView(generic.UpdateView):
#     form_class = UpdateStoryForm
#     model = NewsStory
#     template_name = 'news/updateStory.html'

