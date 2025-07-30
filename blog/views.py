from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from .models import BlogEntry


class BlogEntryListView(ListView):
    model = BlogEntry
    template_name = 'blog/blog_list.html'
    context_object_name = 'blogs'

    def get_queryset(self):
        return BlogEntry.objects.filter(publication_sign=True)


class BlogEntryCreateView(CreateView):
    model = BlogEntry
    fields = ['title', 'content', 'preview', 'publication_sign']
    template_name = 'blog/blog_create.html'
    success_url = reverse_lazy('blog:blogs')


class BlogEntryUpdateView(UpdateView):
    model = BlogEntry
    fields = ['title', 'content', 'preview', 'publication_sign']
    template_name = 'blog/blog_create.html'
    success_url = reverse_lazy('blog:blogs')

    def get_success_url(self):
        return reverse('blog:blog_detail', args=[self.kwargs.get('pk')])


class BlogEntryDeleteView(DeleteView):
    model = BlogEntry
    template_name = 'blog/blog_delete.html'
    success_url = reverse_lazy('blog:blogs')


class BlogEntryDetailView(DetailView):
    model = BlogEntry
    template_name = 'blog/blog_detail.html'
    context_object_name = 'blog'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.number_of_views += 1
        self.object.save()
        return self.object
