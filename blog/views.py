from django.views.generic import ListView, DetailView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView, DayArchiveView, TodayArchiveView
from blog.models import Post

# Search 기능 추가
from django.views.generic import FormView
from blog.forms import PostSearchForm
from django.db.models import Q
from django.shortcuts import render


# Create your views here.
class PostLV(ListView):
    model = Post
    template_name = "blog/post_all.html"
    context_object_name = "posts" #object_list 
    
    paginate_by = 3

class PostDV(DetailView):
    model = Post

class PostAV(ArchiveIndexView):
    model = Post
    date_field = "modify_date"

class PostYAV(YearArchiveView):
    model = Post
    make_object_list = True
    date_field = "modify_date"

class PostMAV(MonthArchiveView):
    model = Post
    date_field = "modify_date"
    month_format = '%m'

class PostDAV(DayArchiveView):
    model = Post
    date_field = "modify_date"
    month_format = '%m'

class PostTAV(TodayArchiveView):
    model = Post
    date_field = "modify_date"

class SearchFV(FormView):
    form_class = PostSearchForm     # forms.py에 생성
    template_name = "blog/post_search.html" 

    def form_valid(self, form):
        searched_word = self.request.POST['search_word']

        post_list = Post.objects.filter(Q(title__icontains=searched_word) | Q(description__icontains=searched_word) | 
                                        Q(content__icontains=searched_word)).distinct()

        # 검색된 결과
        context = {}
        context['form'] = form
        context['search_keyword'] = searched_word
        context['search_list'] = post_list

        return render(self.request, self.template_name, context)