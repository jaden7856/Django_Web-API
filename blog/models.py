from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    objects = models.Manager()
    
    title = models.CharField('TITLE', max_length=50)
    slug = models.SlugField('SLUG', unique=True, allow_unicode=True, help_text='one word for this alias')
    description = models.CharField('DESCRIPTION', max_length=100, blank=True, help_text='simple description text')
    content = models.TextField('CONTENT')
    create_date = models.DateTimeField('Create Date', auto_now_add=True)
    modify_date = models.DateTimeField('Modify Date', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        db_table = 'blog_posts'
        #ordering = ('modify_date', 'author')     # asc & author
        ordering = ('-modify_date',)     # desc


    def get_absolute_url(self):
        return reverse('blog:post_detail', args=(self.slug,)) # -> 1st post -> /blog/post/1st-post

    def get_previous_post(self):
        return self.get_previous_by_modify_date()

    def get_next_post(self):
        return self.get_next_by_modify_date()
    
